import sqlite3
import pandas as pd
import logging
from ingestion_db import ingest_db

logger = logging.getLogger("get_vendor_summary")
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler("logs/get_vendor_summary.log")
fh.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
fh.setFormatter(formatter)

# Avoid duplicate handlers if re-run in interactive session
if not logger.handlers:
    logger.addHandler(fh)


def create_vendor_summary(conn):
    '''this function will merge the different  tables to get the overall vendor summary and adding the new columns in the resultant data'''
    vendor_sales_summary = pd.read_sql_query("""WITH FreightSummary AS (
        SELECT
            VendorNumber,
            SUM(Freight) as FreightCost
        FROM vendor_invoice
        GROUP BY VendorNumber
    ),
    
    PurchaseSummary AS (
        SELECT 
            p.VendorNumber,
            p.VendorName,
            p.Brand,
            p.Description,
            p.PurchasePrice,
            pp.Price as Actualprice,
            pp.Volume,
            SUM(p.Quantity) as TotalPurchaseQuantity,
            SUM(p.Dollars) as TotalPurchaseDollars
        FROM purchases p
        JOIN purchase_prices pp 
            ON p.Brand = pp.Brand
        WHERE p.PurchasePrice > 0
        GROUP BY p.VendorNumber, p.VendorName, p.Brand, p.Description, p.PurchasePrice, pp.Price, pp.volume
    ),
    
    SalesSummary AS (
        SELECT 
            VendorNo,
            Brand,
            SUM(SalesDollars) as TotalsalesDollars,
            SUM(SalesPrice) as TotalSalesPrice,
            SUM(SalesQuantity) as TotalSalesQuantity,
            SUM(ExciseTax) as TotalExciseTax
        FROM Sales
        GROUP BY VendorNo, Brand
    )
    
    SELECT 
        ps.VendorNumber,
        ps.VendorName,
        ps.Brand,
        ps.Description,
        ps.PurchasePrice,
        ps.ActualPrice,
        ps.Volume,
        ps.TotalPurchaseQuantity,
        ps.TotalPurchaseDollars,
        ss.TotalSalesQuantity,
        ss.TotalsalesDollars,
        ss.TotalSalesPrice,
        ss.TotalExciseTax,
        fs.FreightCost
    FROM PurchaseSummary ps
    LEFT JOIN SalesSummary ss
        ON ps.VendorNumber = ss.VendorNo
        AND ps.Brand = ss.Brand
    LEFT JOIN FreightSummary fs
        ON ps.VendorNumber = fs.VendorNumber
    ORDER BY ps.TotalPurchaseDollars DESC""",conn)

    return vendor_sales_summary

def clean_data(df):
    '''this function will clean the data'''
    #Cleaning datatype to float
    df['Volume'] = df['Volume'].astype('float')

    #Filling Missing values with 0
    df.fillna(0,inplace=True)

    #Removing space from categorical columns
    df['VendorName'] = df['VendorName'].str.strip()
    df['Description'] = df['Description'].str.strip()

    #Creating new columns for better analysis
    df['GrossProfit'] = df['TotalsalesDollars'] - df['TotalPurchaseDollars']
    df['ProfitMargin'] = (df['GrossProfit'] / df['TotalsalesDollars'])*100
    df['StockTurnOver'] = df['TotalSalesQuantity'] / df['TotalPurchaseQuantity']
    df['SalesToPurchaseRatio'] = df['TotalsalesDollars'] / df['TotalPurchaseDollars']

    return df

if __name__ == '__main__':
    #Creating database connection
    conn = sqlite3.connect('inventory.db')

    logger.info('Creating Vendor Summary Table.....')
    summary_df = create_vendor_summary(conn)
    logger.info(summary_df.head())

    logger.info('Cleaning Data.....')
    clean_df = clean_data(summary_df)
    logger.info(clean_df.head())
    
    logger.info('Ingesting Data.....')
    ingest_db(clean_df, 'vendor_sales_summary',conn)
    logger.info('Completed')
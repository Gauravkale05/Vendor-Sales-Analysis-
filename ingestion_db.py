import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

logger = logging.getLogger("ingestion_db")
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler("logs/ingestion_db.log")
fh.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
fh.setFormatter(formatter)

if not logger.handlers:
    logger.addHandler(fh)


engine = create_engine('sqlite:///inventory.db')

def ingest_db(df,table_name,engine):
    '''this function will ingest the dataframe into database table'''
    df.to_sql(table_name, con = engine, if_exists = 'replace', index = False) 

def load_raw_data():
    '''This Function will load the CSVs as dataframe and ingest into db'''
    start = time.time()
    for file in os.listdir('data'):
        if '.csv' in file:
            df = pd.read_csv('data/'+file)
            logger.info(f'Ingesting {file} in db')
            ingest_db(df,file[:-4], engine)
        end = time.time()
    total_time = (end - start)/60
    logger.info('Ingestion Complete')
    logger.info(f'Total Time Taken: {total_time} minutes')

if __name__ == '__main__':
    load_raw_data()
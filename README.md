# 📊 Vendor-Sales-Analysis

## 📝 Summary:
This project provides a complete **Vendor Sales Summary and Performance Analysis** pipeline, integrating raw purchase, sales, and freight data into a unified view. It automates data ingestion, cleaning, and transformation, stores results in a **SQLite database**, and delivers actionable insights through exploratory analysis and an interactive **Power BI dashboard**. 🚀

## 🏢 Business Problem:
Organizations often rely on multiple vendors, but their performance is difficult to evaluate because purchase, sales, and freight data are stored in separate systems. Without a consolidated view, decision-makers lack clarity on vendor profitability and efficiency. This leads to challenges such as:  

* ⚖️ Difficulty in identifying which vendors drive growth versus which drain resources.  
* 👀 Limited visibility into the true impact of freight and purchase costs on overall margins.  
* ❌ Making poor purchasing and negotiation decisions because performance metrics like profit margin, stock turnover, and sales-to-purchase ratios are unclear.  

This project directly impacts the business by consolidating data, uncovering vendor-level insights, and enabling smarter, **data-driven decisions** that improve profitability and operational efficiency. 💡

## 🛠️ Methodology:
* 📥 **Data Ingestion** → Load raw CSV files into a SQLite database.  
* 🔗 **Data Integration & Cleaning** → Merge purchases, sales, and freight data; handle missing values and standardize formats.  
* ⚙️ **Feature Engineering** → Create KPIs like Gross Profit, Profit Margin, Stock Turnover, and Sales-to-Purchase Ratio.  
* 📊 **Analysis & Visualization** → Explore insights in Jupyter notebooks and present results in a Power BI dashboard.  

## 💻 Tech Stack:
* Python (Pandas, SQLAlchemy, SQLite3) 🐍  
* SQLite (lightweight database for vendor data) 🗄️  
* Jupyter Notebooks (Exploratory analysis & insights) 📓  
* Power BI (Interactive dashboards) 📈  

## 📸 Dashboard Preview
![Dashboard Preview](https://github.com/Gauravkale05/Vendor-Sales-Analysis-/blob/main/SnapShot%20of%20the%20Dashboard.png)

## 🔑 Key Insights:
* 🏆 **Top Vendors**: Some vendors generate high profit despite moderate sales, while others have high sales but low margins due to freight costs.  
* ⚖️ **Sales-to-Purchase Gaps**: Certain vendors show overstock risks, highlighting the need for optimized procurement.  
* 🚚 **Freight & Profit**: Lower freight costs per unit correlate with higher profit margins, emphasizing cost-effective logistics.  
* 🔄 **Stock Turnover**: Fast-moving products indicate efficient inventory usage; slow-moving items suggest promotional opportunities.  

## 💡 Actionable Insights for Stakeholders
- 💰 **Focus on High-Profit Vendors**: Prioritize vendors with high profit margins for strategic partnerships or bulk orders.  
- 📦 **Negotiate Freight & Costs**: Identify vendors with high freight costs and explore better shipping options or renegotiate terms.  
- 📊 **Optimize Inventory**: Monitor vendors with low sales-to-purchase ratios to reduce overstock and free up working capital.  
- 🛍️ **Promote Slow-Moving Items**: Plan discounts or marketing campaigns for slow-moving products to improve stock turnover.  
- 🤝 **Brand Alignment**: Expand collaboration with brands/vendors that consistently outperform others in profit contribution.  

## 🚀 Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/Gauravkale05/Vendor-Sales-Analysis.git
   cd Vendor-Sales-Analysis
2. Set Up Python Environment
   ```bash
   python -m venv venv
   source venv/bin/activate      # On Linux/macOS
   venv\Scripts\activate         # On Windows
3. Install Dependencies
   ```bash
   pip install -r requirements.txt
4. Run Jupyter Notebooks
   ```bash
   jupyter notebook
5. Open Power BI Dashboard
   * Open Vendor Performace Analysis.pbit in Power BI Desktop.
## 🛣️ Next Steps:
* Real-Time Insights → Connect Power BI directly to the database for live dashboards.
* Predictive Analytics → Build forecasting models for vendor demand, sales trends, and cost optimization.
* Scalability → Move from SQLite to a cloud database (e.g., PostgreSQL, Snowflake) for larger datasets.

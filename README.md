#  BizBuySell Web Scraper  

## 📌 Overview  
This Python-based **web scraper** extracts business listings from **BizBuySell**, focusing on owner-financed and established businesses. It collects details such as **title, location, asking price, cash flow, reason for selling, broker details, and phone numbers** from multiple pages.  

The scraper works in two steps:  
1. **Scrapes main listings** (title, location, asking price, cash flow, and links).  
2. **Extracts additional details** (broker name, reason for selling, and phone number) by visiting individual listing pages.

## 📊 CSV Data Format  

The extracted data is saved in **`listings.csv`** with the following columns:  

| Title                                     | Location          | Asking Price | Cash Flow         | Link                                                                                     | Reason for Selling       | Broker Name                   | Phone Number  |
|-------------------------------------------|-------------------|--------------|-------------------|-----------------------------------------------------------------------------------------|-------------------------|------------------------------|--------------|
| Midsize Lucrative Established Car Dealership | Cook County, IL   | $4,500,000   | $1,199,035       | [Listing](https://www.bizbuysell.com/Business-Opportunity/midsize-lucrative-established-car-dealership/2183786/) | Owner Retiring          | N/A                          | 708-943-7253 |
| Two Explosive Growth Auto Body Shops      | Nassau County, NY | $9,400,000   | $2,300,000       | [Listing](https://www.bizbuysell.com/Business-Opportunity/two-explosive-growth-auto-body-shops/2345250/) | Seller will train       | Vested Business Brokers, Ltd | 855-928-5105 |
| Disaster Restoration Company for Sale     | Virginia          | $4,300,000   | $1,300,000       | [Listing](https://www.bizbuysell.com/Business-Opportunity/disaster-restoration-company-for-sale/2284531/) | Owner wishes to retire | Gavin Raphael                 | 804-781-3155 |


## ⚡ Features  
- **Automated browsing** using **undetected_chromedriver** and **Selenium**.  
- Scrapes **multiple pages (1-6)** dynamically.  
- Extracts **business details & broker contact info**.  
- Saves data in **CSV format** for easy access.  
- Implements **error handling & delays** to avoid detection.  

## 🛠️ Tech Stack  
- **Python**  
- **Selenium** (for web automation)  
- **undetected_chromedriver** (to bypass bot detection)  
- **CSV module** (for data storage)  
- **Random delays** (to simulate human behavior)  

## 🚀 Installation & Setup  

### 1️⃣ Prerequisites  
- Install **Python 3.x**  
- Install **Google Chrome** (ensure it's updated)  

### 2️⃣ Install Required Libraries  
```sh
pip install -r requirements.txt
```

### 3️⃣ Run the Scrapper  
```sh
python scrapper.py
```

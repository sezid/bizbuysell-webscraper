#  BizBuySell Web Scraper  

## 📌 Overview  
This Python-based **web scraper** extracts business listings from **BizBuySell**, focusing on owner-financed and established businesses. It collects details such as **title, location, asking price, cash flow, reason for selling, broker details, and phone numbers** from multiple pages.  

The scraper works in two steps:  
1. **Scrapes main listings** (title, location, asking price, cash flow, and links).  
2. **Extracts additional details** (broker name, reason for selling, and phone number) by visiting individual listing pages.  

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

### 3️⃣ Run the Scrapper  
```sh
python scrapper.py

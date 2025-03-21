import csv
import time
import random
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

# ✅ Define target URL with page numbers from 1 to 6
base_url = "https://www.bizbuysell.com/owner-financed-established-businesses-for-sale/{}/?q=Y2Zmcm9tPTc1MDAwMCZnaWZyb209MTAwMDAwMCZoYmw9ZSZpMj0xMzYsODEsNTcsMjAmcGZyb209MjAwMDAwMA%3D%3D"

# ✅ Initialize CSV file
csv_file = "listings.csv"
csv_headers = ["Title","Location", "Asking Price", "Cash Flow", "Link", "Reason for Selling", "Broker Name", "Phone Number"]

# ✅ Step 1: Scrape data from all 6 pages
def get_driver():
    driver = uc.Chrome(headless=False)
    driver.implicitly_wait(10)
    return driver

def scrape_main_pages():
    driver = get_driver()

    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(csv_headers)

        for page_num in range(1,7):  # Pages from 1 to 6
            url = base_url.format(page_num)
            print(f"🚀 Visiting page {page_num}...")
            driver.get(url)
            time.sleep(random.uniform(3, 5))

            listings = driver.find_elements(By.XPATH, '//a[div[contains(@class, "listing")]]')
            print(f"🔗 Found {len(listings)} listings on page {page_num}.")

            for listing in listings:
                try:
                    link = listing.get_attribute('href')
                    title = listing.find_element(By.TAG_NAME, "h3").text.strip() if listing.find_elements(By.TAG_NAME, "h3") else "N/A"
                    asking_price = listing.find_element(By.XPATH, './/p[contains(@class, "asking-price")]').text.strip() if listing.find_elements(By.XPATH, './/p[contains(@class, "asking-price")]') else "N/A"
                    cash_flow = listing.find_element(By.XPATH, './/p[contains(@class, "cash-flow")]').text.strip() if listing.find_elements(By.XPATH, './/p[contains(@class, "cash-flow")]') else "N/A"
                    location = listing.find_element(By.XPATH,'.//p[contains(@class,"location")]').text.strip() if listing.find_elements(By.XPATH,'.//p[contains(@class,"location")]') else "N/A"
                    writer.writerow([title, location,asking_price, cash_flow, link, "", "", ""])

                except Exception as e:
                    print(f"❌ Error on page {page_num}: {e}")
                    continue
    driver.quit()


# ✅ Step 2: Visit each listing link and scrape additional data
def scrape_inner_pages():
    driver = get_driver()

    # ✅ Open the CSV in append mode to update rows immediately
    with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Skip header

        # ✅ Open another CSV in write mode to update each row instantly
        with open(csv_file, mode='w', newline='', encoding='utf-8') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(headers)  # Write header again

            for row in reader:
                link = row[4]  # Link from CSV
                driver.get(link)
                time.sleep(random.uniform(3, 6))

                try:
                    # ✅ Extract broker name
                    broker_element = driver.find_elements(By.XPATH, './/a[contains(@class,"broker-name")]')
                    broker = broker_element[0].text.strip() if broker_element else "N/A"

                    # ✅ Extract reason for selling
                    reason_element = driver.find_elements(By.XPATH, '(//dd[@class="col-12 col-sm-9 word-break"])[last()]')
                    reason = reason_element[0].text.strip() if reason_element else "N/A"

                    # ✅ Extract phone number (click to reveal)
                    try:
                        span_element = driver.find_element(By.XPATH, "//span[contains(@class,'text-dec-h')]")
                        driver.execute_script("arguments[0].click();", span_element)  # Force click with JS
                        time.sleep(3)
                        phone_element = driver.find_elements(By.XPATH, './/span[contains(@class,"text-dec-h")]')
                        phone = phone_element[0].text.strip() if phone_element else "N/A"
                    except:
                        phone = "N/A"

                    # ✅ Append new data to the row
                    # row.append(reason)
                    # row.append(broker)
                    # row.append(phone)
                    row[5]=reason
                    row[6]=broker
                    row[7]=phone

                except Exception as e:
                    print(f"❌ Error in {link}: {e}")
                    row.extend(["N/A", "N/A", "N/A"])  # In case of failure, fill with N/A
                
                # ✅ Write the updated row immediately
                writer.writerow(row)

    driver.quit()


if __name__ == "__main__":
    scrape_main_pages()
    print("✅ Step 1: Main page data saved to CSV.")

    scrape_inner_pages()
    print("✅ Step 2: Inner page data successfully added.")

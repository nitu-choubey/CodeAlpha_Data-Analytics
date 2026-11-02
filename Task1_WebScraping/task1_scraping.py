# Task 1: Web Scraping using BeautifulSoup and Pandas
# Internship: CodeAlpha Data Analytics

import requests
from bs4 import BeautifulSoup
import pandas as pd

# 1. Target URL (A safe, public website designed for scraping practice)
url = "http://quotes.toscrape.com/"

print("[INFO] Fetching web page data...")
response = requests.get(url)

if response.status_code == 200:
    # 2. Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    quotes_data = []
    
    # 3. Extract relevant data (quotes and authors)
    print("[INFO] Extracting quotes and authors from HTML structure...")
    for item in soup.find_all('div', class_='quote'):
        text = item.find('span', class_='text').get_text()
        author = item.find('small', class_='author').get_text()
        quotes_data.append({'Quote': text, 'Author': author})
        
    # 4. Create a custom dataset using Pandas
    df = pd.DataFrame(quotes_data)
    
    print("\n--- Scraped Data Sample ---")
    print(df.head())
    
    # 5. Save the custom dataset to a CSV file
    csv_filename = 'scraped_quotes.csv'
    df.to_csv(csv_filename, index=False)
    print(f"\n[SUCCESS] Custom dataset successfully saved as '{csv_filename}'!")
    
else:
    print(f"[ERROR] Failed to retrieve webpage. Status code: {response.status_code}")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# List of values
values = [
    "NumA", "NumB", "NumD", "NumG", "NumH", "NumI", "NumJ", "NumM", "NumN", 
    "NumQ", "NumR", "NumU", "Num029", "Num031", "Num034", "Num041", "Num045", 
    "Num048", "Num049", "Num055", "Num062", "Num069", "Num071", "Num072", "Num073", 
    "Num076", "Num078", "Num080", "Num083", "Num090", "Num094", "Num097", "Num098", 
    "Num104", "Num111", "Num118", "Num125"
]

# Chrome profile directory
chrome_profile_path = 'C:/Users/NowocinskiFilip/AppData/Local/Google/Chrome/User Data'

# Chrome options
chrome_options = Options()
chrome_options.add_argument("user-data-dir=" + chrome_profile_path)

# Chrome service
chrome_service = Service(r"C:\Users\NowocinskiFilip\Desktop\chromedriver-win64\chromedriver.exe")

# Initialize Chrome driver
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Open the website
driver.get("https://steptask.koyama-kk.co.jp/pleasanter/items/1828889")

# Wait for the page to load after login
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[id^='Results_NumA']")))

# Function to scrape data for a given value
def scrape_data(value):
    try:
        placeholder = driver.find_element(By.CSS_SELECTOR, f"input[id^='Results_{value}']")
        return placeholder.get_attribute('placeholder')
    except:
        return None

# Scraping data for all values
data = {value: scrape_data(value) for value in values}

# Creating a table
df = pd.DataFrame(list(data.items()), columns=['Value', 'Data'])

# Displaying the table
print(df)

# Close the browser
driver.quit()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

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


# Function to scrape data for all input elements
def scrape_data():
    try:
        elements = driver.find_elements(By.TAG_NAME, 'input')
        data = {}
        for element in elements:
            element_id = element.get_attribute('id')
            placeholder = element.get_attribute('placeholder')
            data[element_id] = placeholder
        return data
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Scraping data for all elements
data = scrape_data()

# Creating a table and saving it to CSV
if data:
    df = pd.DataFrame(list(data.items()), columns=['ID', 'Placeholder'])
    # Save the DataFrame to a CSV file
    df.to_csv('input_elements_data.csv', index=False)
    print("Data has been saved to input_elements_data.csv")
else:
    print("No data found or an error occurred.")
print(df)

# Close the browser
driver.quit()

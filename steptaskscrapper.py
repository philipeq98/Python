from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Path to your ChromeDriver
driver_path = r"C:\Users\NowocinskiFilip\Desktop\chromedriver-win64\chromedriver.exe"

# Create a Service object
service = Service(driver_path)

# Path to your Chrome user data directory
user_data_dir = r'C:\Users\NowocinskiFilip\AppData\Local\Google\Chrome\User Data'
profile_dir = 'Default'  # Replace 'Default' with the profile name if different

# Create a ChromeOptions object and configure it to use your Chrome profile
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'--user-data-dir={user_data_dir}')
chrome_options.add_argument(f'--profile-directory={profile_dir}')
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--remote-debugging-port=9222')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')

# Initialize the Chrome driver with the Service object
driver = webdriver.Chrome(service=service, options=chrome_options)

time.sleep(5)

# URL of the website you want to scrape
url = 'https://steptask.koyama-kk.co.jp/pleasanter/items/1828224#FieldSetTab5'

# Open the URL
driver.get(url)

# Find the element with id="Results_NumG" within the fieldset with id="FieldsetTab5"
fieldset = driver.find_element(By.ID, 'FieldSetTab5')
result_elem = fieldset.find_element(By.ID, 'Results_NumG')

# Get the 'value' and 'placeholder' attributes
value_attr = result_elem.get_attribute('value')
placeholder_attr = result_elem.get_attribute('placeholder')

# Print the attributes
print(f'value: {value_attr}')
print(f'placeholder: {placeholder_attr}')

# Close the browser
driver.quit()

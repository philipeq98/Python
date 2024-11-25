import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Define your lists
first_list = [
    1828222, 1828217, 1828218, 1828219, 1828220, 1828221, 1828223, 1828224, 1828225, 1828226,
    1828227, 1828228, 1828269, 1828270, 1828271, 1828272, 1828273, 1828274, 1828275, 1828276,
    1828277, 1828278, 1828279, 1828280, 1828879, 1828880, 1828881, 1828882, 1828883, 1828884,
    1828885, 1828886, 1828887, 1828888, 1828889, 1828890
]

# Define a dictionary mapping first list values to year-month pairs
year_month_dict = {
    1828222: '2023/10', 1828217: '2024/03', 1828218: '2024/02', 1828219: '2024/01',
    1828220: '2023/12', 1828221: '2023/11', 1828223: '2023/09', 1828224: '2023/08',
    1828225: '2023/07', 1828226: '2023/06', 1828227: '2023/05', 1828228: '2023/04',
    1828269: '2023/03', 1828270: '2023/02', 1828271: '2023/01', 1828272: '2022/12',
    1828273: '2022/11', 1828274: '2022/10', 1828275: '2022/09', 1828276: '2022/08',
    1828277: '2022/07', 1828278: '2022/06', 1828279: '2022/05', 1828280: '2022/04',
    1828879: '2022/03', 1828880: '2022/02', 1828881: '2022/01', 1828882: '2021/12',
    1828883: '2021/11', 1828884: '2021/10', 1828885: '2021/09', 1828886: '2021/08',
    1828887: '2021/07', 1828888: '2021/06', 1828889: '2021/05', 1828890: '2021/04'}

second_list = [
    'Results_NumG', 'Results_NumH', 'Results_NumI', 'Results_NumJ', 'Results_NumM', 'Results_NumN',
    'Results_NumO', 'Results_NumP'
]

data = []

# Path to your ChromeDriver executable
driver_path = r"C:\Users\NowocinskiFilip\Desktop\chromedriver-win64\chromedriver.exe"

# Path to your Chrome user data directory
user_data_dir = 'C:/Users/NowocinskiFilip/AppData/Local/Google/Chrome/User Data'
profile_dir = 'Default'  # Replace 'Default' with the profile name if different

# Create a Service object
service = Service(driver_path)

# Create a ChromeOptions object and configure it to use your Chrome profile
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'--user-data-dir={user_data_dir}')
chrome_options.add_argument(f'--profile-directory={profile_dir}')
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--remote-debugging-port=9222')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')

# Initialize the Chrome driver with the Service object and ChromeOptions
driver = webdriver.Chrome(service=service, options=chrome_options)

# Optional: Add a delay to ensure the profile loads properly
time.sleep(5)

# Base URL for scraping
base_url = 'https://steptask.koyama-kk.co.jp/pleasanter/items/'

# Save the dataframe to an Excel file on the desktop
desktop_path = 'C:/Users/NowocinskiFilip/Desktop/'
excel_file_path = desktop_path + 'scraped_data.xlsx'

# Loop over each combination of URLs and element IDs
for first_value in first_list:
    year_month = year_month_dict.get(first_value, '')
    for second_id in second_list:
        # Construct the URL
        url = f'{base_url}{first_value}#FieldSetTab5'

        # Open the URL
        driver.get(url)

        # Wait for the fieldset with id="FieldsetTab5" to become visible
        # Wait for a maximum of 10 seconds
        fieldset = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'FieldSetTab5')))

        # Find the element with the specified ID within the fieldset
        result_elem = fieldset.find_element(By.ID, second_id)

        # Get the 'value' and 'placeholder' attributes
        value_attr = result_elem.get_attribute('value')
        placeholder_attr = result_elem.get_attribute('placeholder')

        # Append the data to the list
        data.append([first_value, year_month, second_id, value_attr, placeholder_attr])

# Close the browser
driver.quit()

# Create a DataFrame from the collected data
df = pd.DataFrame(data, columns=['First_Value', 'Period', 'Second_ID', 'Value', 'Placeholder'])

# Print the dataframe
print(df)

# Save the dataframe to Excel
df.to_excel(excel_file_path, index=False)

print(f"DataFrame saved to {excel_file_path}")
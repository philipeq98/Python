import pandas as pd
from googletrans import Translator

# Load the Excel file into a pandas DataFrame
df = pd.read_excel(r"C:\Users\NowocinskiFilip\Desktop\DATA ENCODED\master\workbook.xlsx")

# Create a dictionary to store translations
translation_dict = {}

# Function to translate text from Japanese to English
def translate_text(text):
    if text not in translation_dict:
        print(f"Translating: {text}")
        translator = Translator()
        translation = translator.translate(text, src='ja', dest='en')
        translation_dict[text] = translation.text
    return translation_dict[text]

# Iterate over unique values in the first 3 columns, translate them, and store in the dictionary
for i in range(3):  # assuming first 3 columns are to be translated
    unique_values = df.iloc[:, i].unique()
    for value in unique_values:
        translate_text(value)

# Replace values in the DataFrame using the translation dictionary
for i in range(3):  # assuming first 3 columns are to be translated
    df.iloc[:, i] = df.iloc[:, i].map(translation_dict)

# Save the DataFrame back to Excel
df.to_excel(r"C:\Users\NowocinskiFilip\Desktop\DATA ENCODED\master\workbook2.xlsx", index=False)

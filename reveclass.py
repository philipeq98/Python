import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('revenueclassification.csv')

# Define a function to classify each item based on the '正式科目名'
def classify_item(row):
    subject = row['正式科目名']
    
    # Ensure that the '正式科目名' is a string (handle NaN or non-string values)
    if isinstance(subject, str):
        if '加工' in subject:
            return '加工収入'
        elif '賃貸料' in subject or 'レンタル' in subject:
            return 'レンタル収入'
        elif '小山' in subject:
            return '子会社間取引'
        elif '役務提供' in subject or '業務委託収入' in subject:
            return 'その他'
        elif '販売品' in subject:
            return '販売品'
        elif 'その他' in subject or '雑収入' in subject:
            return 'その他'
        elif '医療' in subject:
            return '医療関連'
        else:
            return 'その他'
    else:
        # Handle NaN or non-string cases (e.g., return '未分類' for NaN)
        return 'その他'

# Apply the classification function to each row and create a new '分類' column
df['分類'] = df.apply(classify_item, axis=1)

# Save the updated DataFrame to an Excel file
df.to_excel('revenueclassification2.xlsx', index=False)

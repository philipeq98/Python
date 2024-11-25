import pandas as pd

# Step 1: Read the data from the specified sheet in the Excel file
# Replace 'your_file.xlsx' with your actual file path and 'Sheet1' with your sheet name
file_path = r"C:\Users\NowocinskiFilip\Desktop\Data Source\総勘定元帳_マスタデータ.xlsx"
sheet_name = 'M_統一科目リスト'  # Change this to the name of the sheet you want to read
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Step 2: Extract unique pairs
unique_pairs = df[['コード', '正式科目名']].drop_duplicates()

# Step 3: Format the pairs
formatted_pairs = unique_pairs.apply(lambda row: f"{row['コード']},{row['コード']}-{row['正式科目名']}", axis=1)

# Step 4: Print the results
for pair in formatted_pairs:
    print(pair)

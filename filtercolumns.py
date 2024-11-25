import pyodbc
import pandas as pd

# Database connection parameters
server = 'steptask.koyama-kk.co.jp,14330'
database = 'Implem.Pleasanter'
username = 'ctp_n.filip_reader'
password = 'dPJpERAKnm8#RQuhRhmjTv-Lqx99Ny'
driver= '{ODBC Driver 17 for SQL Server}'

# Establishing the connection
conn = pyodbc.connect(
    'DRIVER=' + driver + ';SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password
)

# SQL query to fetch data
query = """
SELECT *
FROM [dbo].[V_CTP_Results]
WHERE [SiteId] = 1825957
"""

# Fetching data into a pandas DataFrame
df = pd.read_sql(query, conn)

# Closing the connection
conn.close()

# Removing columns where all values are null
df_cleaned = df.dropna(axis=1, how='all')

# Display the cleaned DataFrame
print(df_cleaned)

# Optionally, you can save the cleaned DataFrame to a new CSV file
df_cleaned.to_csv('cleaned_results.csv', index=False)

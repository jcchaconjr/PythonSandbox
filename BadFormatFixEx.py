import pandas as pd

df = pd.read_csv('baddata.csv')

df['Date'] = pd.to_datetime(df['Date'])

print(df.to_string())

# Row 26 will get its date format fixed...
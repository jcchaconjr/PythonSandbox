import pandas as pd

df = pd.read_csv('baddata.csv')

new_df = df.dropna()

print(new_df.to_string())

#Notice in the result that some rows have been removed (row 18, 22 and 28).

#These rows had cells with empty values.

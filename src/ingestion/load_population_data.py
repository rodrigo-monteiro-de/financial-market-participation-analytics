import pandas as pd

FILE_PATH = "data/bronze/population_total.csv"

df = pd.read_csv(FILE_PATH,skiprows = 4)

#print("\n=== DATASET INFORMATION===")
#print(f"Rows:{df.shape[0]}")
#print(f"Columns:{df.shape[1]}")

#print("\n=== FIRST 5 rows===")
#print(df.head())

print(df.columns[4])
print(df.columns[5])
print(df.columns[6])

year_columns = df.columns[4:-1]

print(year_columns)

print(len(year_columns))




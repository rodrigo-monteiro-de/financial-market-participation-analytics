import pandas as pd

INPUT_FILE = "data/bronze/population_total.csv"

df = pd.read_csv(INPUT_FILE,skiprows=4)

print(f"Rows before transformation: {df.shape[0]}")
print(f"Coluns before transformation:{df.shape[1]}")
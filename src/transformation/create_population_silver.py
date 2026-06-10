import pandas as pd

#Leitura do arquivo Bronze
INPUT_FILE = "data/bronze/population_total.csv"

df = pd.read_csv(INPUT_FILE,skiprows=4)

print(f"Rows before transformation: {df.shape[0]}")
print(f"Coluns before transformation:{df.shape[1]}")

#excluir coluna "unnamed 70"
df = df.drop(columns=["Unnamed: 70"])
print(f"Columns after cleanup:{df.shape[1]}")

#for col in df.columns:
#    print(f"'{col}'")
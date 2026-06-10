import pandas as pd

#Leitura do arquivo Bronze
INPUT_FILE = "data/bronze/population_total.csv"

df = pd.read_csv(INPUT_FILE, skiprows=4)

print(f"Input dataset: {df.shape}")

df = df.drop(columns=["Unnamed: 70"])

year_columns = df.columns[4:]

silver_df = pd.melt(
    df,
    id_vars=["Country Name", "Country Code"],
    value_vars=year_columns,
    var_name="Year",
    value_name="Population"
)

print(f"Silver dataset: {silver_df.shape}")

silver_df.to_csv(
    "data/silver/population_by_country_year.csv",
    index=False
)

print("Silver layer generated successfully.")

#testes 

loaded_df = pd.read_csv(
    "data/silver/population_by_country_year.csv"
)

print(loaded_df.shape)
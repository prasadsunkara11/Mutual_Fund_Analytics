import pandas as pd

# Read file
df = pd.read_csv(
    "data/raw/NAVAll.csv",
    header=None
)

print("Original Shape:", df.shape)

# Remove empty rows
df = df.dropna()

# Split single column using ;
df = df[0].str.split(";", expand=True)

print("After Split:", df.shape)
print(df.head())
# Keep only valid scheme rows
df = df[
    df[0].astype(str).str.isdigit()
]

df = df.reset_index(drop=True)

print("Valid Records:", df.shape)
print(df.head())
df.columns = [
    "scheme_code",
    "isin_growth",
    "isin_reinvestment",
    "scheme_name",
    "nav",
    "date"
]
df["scheme_code"] = df["scheme_code"].astype(int)

df["nav"] = pd.to_numeric(
    df["nav"],
    errors="coerce"
)

df["date"] = pd.to_datetime(
    df["date"],
    format="%d-%b-%Y"
)
print(df.info())

print(df.isnull().sum())
print(df.duplicated().sum())

# Save cleaned data
df.to_csv(
    "data/processed/nav_history.csv",
    index=False
)

print("nav_history.csv created successfully!")
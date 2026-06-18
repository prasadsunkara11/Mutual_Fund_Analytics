import pandas as pd

schemes = pd.read_csv(
    "data/processed/schemes.csv"
)

top_funds = (
    schemes
    .groupby("fund_house")
    .head(5)
)

top_funds.to_csv(
    "data/processed/top_funds.csv",
    index=False
)

print(top_funds.shape)
print(top_funds.head())
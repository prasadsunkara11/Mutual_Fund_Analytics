import pandas as pd
import numpy as np

funds = pd.read_csv(
    "data/processed/top_funds.csv"
)

dates = pd.date_range(
    start="2023-01-01",
    end="2026-06-17",
    freq="B"
)

records = []

for _, row in funds.iterrows():

    nav = np.random.uniform(10, 100)

    for d in dates:

        change = np.random.normal(
            0.0005,
            0.01
        )

        nav = nav * (1 + change)

        records.append([
            row["scheme_code"],
            d.date(),
            round(nav, 2)
        ])

historical_nav = pd.DataFrame(
    records,
    columns=[
        "scheme_code",
        "date",
        "nav"
    ]
)

historical_nav.to_csv(
    "data/processed/historical_nav.csv",
    index=False
)

print(historical_nav.shape)
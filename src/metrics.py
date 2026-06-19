import pandas as pd
import numpy as np
df = pd.read_csv(
    "data/processed/historical_nav.csv"
)

df["date"] = pd.to_datetime(
    df["date"]
)

df = df.sort_values(
    ["scheme_code", "date"]
)

print(df.head())
df["daily_return"] = (
    df
    .groupby("scheme_code")["nav"]
    .pct_change()
)
annual_return = (
    df
    .groupby("scheme_code")["daily_return"]
    .mean()
    * 252
)
first_nav = (
    df
    .groupby("scheme_code")["nav"]
    .first()
)

last_nav = (
    df
    .groupby("scheme_code")["nav"]
    .last()
)

years = (
    (
        df["date"].max()
        -
        df["date"].min()
    ).days
) / 365

cagr = (
    (last_nav / first_nav)
    ** (1 / years)
) - 1
volatility = (
    df
    .groupby("scheme_code")["daily_return"]
    .std()
    * np.sqrt(252)
)
risk_free_rate = 0.06

sharpe_ratio = (
    annual_return
    -
    risk_free_rate
) / volatility
def calculate_drawdown(group):

    cumulative = (
        1 +
        group["daily_return"]
        .fillna(0)
    ).cumprod()

    peak = cumulative.cummax()

    drawdown = (
        cumulative -
        peak
    ) / peak

    return drawdown.min()


max_drawdown = (
    df
    .groupby("scheme_code")
    .apply(calculate_drawdown)
)
metrics = pd.DataFrame({

    "annual_return":
        annual_return,

    "cagr":
        cagr,

    "volatility":
        volatility,

    "sharpe_ratio":
        sharpe_ratio,

    "max_drawdown":
        max_drawdown

})

metrics = (
    metrics
    .reset_index()
)

print(metrics.head())
metrics.to_csv(
    "data/processed/fund_metrics.csv",
    index=False
)

print("fund_metrics.csv created!")

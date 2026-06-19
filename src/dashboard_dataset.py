import pandas as pd
import sqlite3

conn = sqlite3.connect(
    "database/nifty100.db"
)

schemes = pd.read_sql(
    "SELECT * FROM schemes",
    conn
)

metrics = pd.read_csv(
    "data/processed/fund_metrics.csv"
)
dashboard = pd.merge(
    schemes,
    metrics,
    on="scheme_code",
    how="inner"
)

print(dashboard.head())
dashboard["fund_rank"] = (
    dashboard["sharpe_ratio"]
    .rank(
        ascending=False,
        method="dense"
    )
)
q1 = dashboard["volatility"].quantile(0.33)
q2 = dashboard["volatility"].quantile(0.66)

def risk_category(vol):
    if vol <= q1:
        return "Low"
    elif vol <= q2:
        return "Medium"
    else:
        return "High"

dashboard["risk_category"] = (
    dashboard["volatility"]
    .apply(risk_category)
)
print(
    dashboard["risk_category"].value_counts()
)
dashboard.to_csv(
    "data/processed/dashboard_data.csv",
    index=False
)

print("Dashboard dataset created!")

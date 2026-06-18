import pandas as pd
import sqlite3

conn = sqlite3.connect("database/nifty100.db")

schemes = pd.read_csv(
    "data/processed/schemes.csv"
)

nav = pd.read_csv(
    "data/processed/nav_history.csv"
)

schemes.to_sql(
    "schemes",
    conn,
    if_exists="replace",
    index=False
)

nav.to_sql(
    "nav_history",
    conn,
    if_exists="replace",
    index=False
)

print("Tables loaded successfully!")

query = """
SELECT
category,
COUNT(*) as total_funds
FROM schemes
GROUP BY category
ORDER BY total_funds DESC
"""

result = pd.read_sql(
    query,
    conn
)

print(result)

conn.close()
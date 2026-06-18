import pandas as pd

df = pd.read_csv(
    "data/processed/nav_history.csv"
)

print(df.shape)
print(df.head())
schemes = df[
    ["scheme_code", "scheme_name"]
].drop_duplicates()

print("Unique Schemes:", schemes.shape)
def get_fund_house(name):
    words = name.split()

    if len(words) >= 4:
        return " ".join(words[:4])

    return name


schemes["fund_house"] = (
    schemes["scheme_name"]
    .apply(get_fund_house)
)
def get_category(name):

    name = name.lower()

    if "equity" in name:
        return "Equity"

    elif "debt" in name:
        return "Debt"

    elif "liquid" in name:
        return "Liquid"

    elif "hybrid" in name:
        return "Hybrid"

    elif "index" in name:
        return "Index"

    elif "overnight" in name:
        return "Overnight"

    else:
        return "Other"


schemes["category"] = (
    schemes["scheme_name"]
    .apply(get_category)
)
print(schemes.head())

print("\nCategories:")
print(
    schemes["category"]
    .value_counts()
)
schemes.to_csv(
    "data/processed/schemes.csv",
    index=False
)

print("schemes.csv created successfully!")

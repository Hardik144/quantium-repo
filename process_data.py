import pandas as pd
from pathlib import Path

DATA_DIR = Path("data")

# Read all CSV files
csv_files = list(DATA_DIR.glob("*.csv"))
dfs = [pd.read_csv(file) for file in csv_files]

# Combine into one DataFrame
df = pd.concat(dfs, ignore_index=True)

# ---- FIX 1: Clean product column ----
df["product"] = df["product"].str.strip().str.lower()

# Keep only pink morsel
df = df[df["product"] == "pink morsel"]

# ---- FIX 2: Convert price to numeric ----
df["price"] = (
    df["price"]
    .str.replace("$", "", regex=False)
    .astype(float)
)

# Quantity should already be numeric, but make sure
df["quantity"] = df["quantity"].astype(int)

# Create Sales column
df["Sales"] = df["price"] * df["quantity"]

# Select final columns
final_df = df[["Sales", "date", "region"]].rename(
    columns={"date": "Date", "region": "Region"}
)

# Save output
final_df.to_csv(DATA_DIR / "final_output.csv", index=False)

print("✅ final_output.csv created successfully")
print(final_df.head())

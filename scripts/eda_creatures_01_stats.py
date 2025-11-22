import pandas as pd

# ============================
# Import
# ============================
df = pd.read_csv("data/raw/creatures_raw_dataset.csv", sep="\\")

# Minimal cleaning (no more at this stage)
df = df.drop(columns=["Unnamed: 0", "Unnamed: 22"])
df.columns = [c.strip() for c in df.columns]

# ============================
# Descriptive statistics
# ============================

print("\n=== INFO ===")
print(df.info())

print("\n=== HEAD ===")
print(df.head())

print("\n=== DESCRIBE (NUM) ===")
print(df.describe())

print("\n=== DESCRIBE (ALL) ===")
print(df.describe(include='all'))

print("\n=== VALUE COUNTS ===")
categorical_cols = ['author', 'archetype', 'death_status', 'gender', 'social_status', 'role_importance']
for col in categorical_cols:
    print(f"\n--- {col} ---")
    print(df[col].value_counts())

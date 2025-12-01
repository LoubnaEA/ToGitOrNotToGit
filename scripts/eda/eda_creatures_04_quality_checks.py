import pandas as pd

# =========================================
# Load cleaned dataset
# =========================================
df = pd.read_csv("data/processed/creatures_clean.csv")

print("\n=== SHAPE ===")
print(df.shape)

print("\n=== COLUMNS ===")
print(df.columns.tolist())

# =========================================
# Check for missing values
# =========================================
print("\n=== MISSING VALUES ===")
print(df.isna().sum())

# =========================================
# Check duplicates
# =========================================
duplicates = df.duplicated().sum()
print(f"\n=== DUPLICATES FOUND: {duplicates} ===")

# Optional: display duplicate rows
if duplicates > 0:
    print(df[df.duplicated()])

# =========================================
# Validate categorical consistency
# =========================================
categorical_cols = [
    "author", "archetype", "death_status", 
    "gender", "social_status", "role_importance"
]

print("\n=== UNIQUE VALUES PER CATEGORICAL COLUMN ===")
for col in categorical_cols:
    print(f"\n--- {col} ---")
    print(df[col].value_counts(dropna=False))

# =========================================
# Validate numeric ranges
# =========================================
numeric_cols = ["number_of_characters_in_play", "death_status_encoded"]

print("\n=== NUMERIC SUMMARY ===")
print(df[numeric_cols].describe())

# =========================================
# Check for out-of-range values
# =========================================
print("\n=== OUT-OF-RANGE CHECK: death_status_encoded ===")
invalid_encoded = df[
    ~df["death_status_encoded"].isin([0, 1, None])
]

print(invalid_encoded if not invalid_encoded.empty 
      else "No invalid encoded values detected.")

# =========================================
# Quick logical checks
# =========================================

# Ex : characters in a play should be > 0
invalid_characters = df[df["number_of_characters_in_play"] <= 0]

print("\n=== LOGICAL CHECK: Characters per play > 0 ===")
print(invalid_characters if not invalid_characters.empty 
      else "All values valid.")

# =========================================
# Final OK message
# =========================================
print("\n✓ Step 4 complete: Dataset validated and ready for analysis / GitHub.")

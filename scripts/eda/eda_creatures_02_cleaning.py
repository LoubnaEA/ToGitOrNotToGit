import pandas as pd

# =========================================
# Load raw dataset
# =========================================
df = pd.read_csv("data/raw/creatures_raw_dataset.csv", sep="\\")

# Remove extra unnamed columns + strip whitespace
df = df.drop(columns=["Unnamed: 0", "Unnamed: 22"])
df.columns = [c.strip() for c in df.columns]

# =========================================
# Keep only allowed authors (remove intrus/unknown)
# =========================================
allowed_authors = [
    # Major
    "William Shakespeare", "Ben Jonson", "Thomas Middleton",
    "John Webster", "Christopher Marlowe", "John Fletcher", "Francis Beaumont",
    # Secondary
    "Dekker", "Greene", "Chapman", "Ford", "Heywood", "Marston",
    "Massinger", "Rowley", "Shirley", "Lyly", "Nashe", "Peele"
]

df = df[df["author"].isin(allowed_authors)]

# =========================================
# Normalize key categorical fields
# =========================================
# Strip spaces and standardize case where appropriate
categorical_cols = ['author', 'archetype', 'death_status', 
                    'gender', 'social_status', 'role_importance']

for col in categorical_cols:
    df[col] = df[col].astype(str).str.strip()

# Uniform case for specific fields
df['death_status'] = df['death_status'].str.lower()
df['gender'] = df['gender'].str.lower()

# =========================================
# Encode death_status for advanced analysis
#    (0 = alive, 1 = dead)
# =========================================
death_map = {
    "alive": 0,
    "dead": 1,
    "unknown": None,         # Handle unexpected cases gracefully
    "": None
}

df["death_status_encoded"] = df["death_status"].map(death_map)

# =========================================
# Expand / clean traits if present
# 		(e.g., splitting comma-separated fields)
# =========================================
traits_col = "traits" if "traits" in df.columns else None

if traits_col:                # Normalize spacing and split into lists
    df[traits_col] = (
        df[traits_col]
        .astype(str)
        .str.replace(r"\s*,\s*", ",", regex=True)
        .str.split(",")
    )

# =========================================
# Fix numeric columns and missing values
# =========================================
numeric_cols = ["number_of_characters_in_play"]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Simple missing-value handling (non-destructive)
df = df.fillna({
    "social_status": "unknown",
    "role_importance": "unknown"
})

# =========================================
# Export cleaned dataset
# =========================================
output_path = "data/processed/creatures_clean.csv"
df.to_csv(output_path, index=False)

print(f"✓ Cleaning complete. File saved to: {output_path}")


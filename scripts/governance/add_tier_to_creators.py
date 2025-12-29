import pandas as pd

INPUT_PATH = "data/raw/creators_raw_dataset.csv"
OUTPUT_PATH = "data/processed/creators_with_tier.csv"

# Source column (raw schema) 
AUTHOR_COLUMN = "Author"

# Tier mapping (source of truth) 
AUTHOR_TIER_MAPPING = {
    "William Shakespeare": "A",
    "Christopher Marlowe": "A",
    "Ben Jonson": "A",
    "John Webster": "A",

    "Thomas Middleton": "B",
    "Thomas Kyd": "B",
    "John Ford": "B",
    "Francis Beaumont": "B",
    "John Fletcher": "B",
    "Philip Massinger": "B",

    "Thomas Dekker": "C",
    "Robert Greene": "C",
    "John Lyly": "C",
    "Thomas Heywood": "C",
    "John Marston": "C",
    "Thomas Nashe": "C",
    "George Peele": "C",
    "George Chapman": "C",
    "William Rowley": "C",
    "James Shirley": "C",
}

# Load dataset 
df = pd.read_csv(INPUT_PATH)

# Apply tier mapping 
df["tier"] = df[AUTHOR_COLUMN].map(AUTHOR_TIER_MAPPING)

# Validation : no missing tiers 
missing = df[df["tier"].isna()]
if not missing.empty:
    raise ValueError(
        f"❌ Tier missing for the following authors :\n{missing[AUTHOR_COLUMN].unique()}"
    )

# Save output
df.to_csv(OUTPUT_PATH, index=False)

print("✅ Tier column successfully added and validated")

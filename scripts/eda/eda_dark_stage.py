import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =========================================
# Load dataset
# =========================================
df = pd.read_csv("data/raw/dark_stage_raw_dataset.md", sep="\\")

# Minimal cleaning
df.columns = [c.strip() for c in df.columns]

# =========================================
# Normalize categorical columns
# =========================================
categorical_cols = ['author', 'archetype', 'death_status', 'gender']
for col in categorical_cols:
    df[col] = df[col].astype(str).str.strip().str.lower()

# Encode death_status
death_map = {"alive":0, "dead":1, "unknown":None, "":None}
df['death_status_encoded'] = df['death_status'].map(death_map)

# =========================================
# Basic Stats
# =========================================
print("\n=== INFO ===")
print(df.info())

print("\n=== HEAD ===")
print(df.head())

print("\n=== DESCRIBE ===")
print(df.describe(include='all'))

for col in categorical_cols:
    print(f"\n--- {col} value counts ---")
    print(df[col].value_counts())

# =========================================
# Visualizations
# =========================================
plt.figure(figsize=(6,4))
sns.countplot(data=df, x='death_status')
plt.title('Death Status Distribution')
plt.show()

plt.figure(figsize=(8,4))
sns.countplot(data=df, y='archetype', order=df['archetype'].value_counts().index)
plt.title('Archetype Distribution')
plt.show()

plt.figure(figsize=(8,4))
sns.countplot(data=df, y='author', order=df['author'].value_counts().index)
plt.title('Characters per Author')
plt.show()

# =========================================
# Quality Checks
# =========================================
print("\n=== Missing Values ===")
print(df.isna().sum())

print("\n=== Duplicates ===")
print(df.duplicated().sum())

numeric_cols = ['death_status_encoded']
print("\n=== Numeric Summary ===")
print(df[numeric_cols].describe())

print("\n✓ EDA complete for dark_stage dataset")

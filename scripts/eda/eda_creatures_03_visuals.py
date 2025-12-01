import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =========================================
# Load cleaned dataset
# =========================================
df = pd.read_csv("data/processed/creatures_clean.csv")

# =========================================
# Simple Distributions
# =========================================

# Death status distribution
plt.figure(figsize=(6,4))
sns.countplot(data=df, x="death_status", order=df["death_status"].value_counts().index)
plt.title("Death Status Distribution")
plt.xlabel("Death Status")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# Encoded death status distribution
plt.figure(figsize=(6,4))
sns.countplot(data=df, x="death_status_encoded")
plt.title("Encoded Death Status (0=alive, 1=dead)")
plt.xlabel("death_status_encoded")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# Archetype distribution
plt.figure(figsize=(8,5))
sns.countplot(
    data=df,
    y="archetype",
    order=df["archetype"].value_counts().index
)
plt.title("Archetype Distribution")
plt.xlabel("Count")
plt.ylabel("Archetype")
plt.tight_layout()
plt.show()

# Author distribution
plt.figure(figsize=(8,5))
sns.countplot(
    data=df,
    y="author",
    order=df["author"].value_counts().index
)
plt.title("Characters per Author")
plt.xlabel("Count")
plt.ylabel("Author")
plt.tight_layout()
plt.show()

# =========================================
# Numeric distributions
# =========================================

# Nber of characters per play
plt.figure(figsize=(6,4))
sns.histplot(df["number_of_characters_in_play"], bins=15)
plt.title("Distribution: Number of Characters in Play")
plt.xlabel("Number of Characters")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# =========================================
# Optional pairplot (quick overview)
# =========================================

# Only run if dataset isn’t too large
# sns.pairplot(df[["number_of_characters_in_play", "death_status_encoded"]])
# plt.show()

print("✓ Step 3 complete: Visualizations generated.")

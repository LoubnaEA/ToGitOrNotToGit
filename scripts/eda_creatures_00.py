

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Import CSV
df = pd.read_csv("data/raw/creatures_raw_dataset.csv", sep="\\")

print(df.head())
print(df.info())

# 2. Nettoyer colonnes inutiles et espaces
df = df.drop(columns=["Unnamed: 0", "Unnamed: 22"])
df.columns = [c.strip() for c in df.columns]

print(df.head())

# Statistiques descriptives pour colonnes numériques
print(df.describe())

# Comptage des valeurs uniques pour certaines colonnes
print(df['author'].value_counts())
print(df['archetype'].value_counts())
print(df['death_status'].value_counts())

# Visualisation simple (optionnel)
df['death_status'].value_counts().plot(kind='bar')
plt.show()

# 3. Aperçu des données
print("=== Head ===")
print(df.head())
print("\n=== Info ===")
print(df.info())
print("\n=== Statistiques descriptives ===")
print(df.describe(include='all'))

# 4. Valeurs uniques et distributions pour colonnes clés
categorical_cols = ['author', 'archetype', 'death_status', 'gender', 'social_status', 'role_importance']
for col in categorical_cols:
    print(f"\n--- {col} value counts ---")
    print(df[col].value_counts())

# 5. Visualisations simples
# a) Distribution des morts vs survivants
plt.figure(figsize=(6,4))
sns.countplot(data=df, x='death_status', palette='coolwarm')
plt.title('Death Status Distribution')
plt.show()

# b) Distribution des archétypes
plt.figure(figsize=(8,4))
sns.countplot(data=df, y='archetype', order=df['archetype'].value_counts().index, palette='viridis')
plt.title('Archetype Distribution')
plt.show()

# c) Nombre de personnages par auteur
plt.figure(figsize=(8,4))
sns.countplot(data=df, y='author', order=df['author'].value_counts().index, palette='magma')
plt.title('Number of Characters per Author')
plt.show()

# 6. Analyse rapide de corrélations
numeric_cols = ['number_of_characters_in_play']
print("\n=== Numeric Summary ===")
print(df[numeric_cols].describe())

# Histogramme du nombre de personnages par play
plt.figure(figsize=(6,4))
sns.histplot(df['number_of_characters_in_play'], bins=15, kde=False, color='skyblue')
plt.title('Number of Characters in Play')
plt.show()

# Visualization Layer

Central repository for finalized visual assets used across documentation, analysis, reports and GitHub presentation.  
Ensures consistency, traceability and clean separation between **production-ready visuals** and **playground outputs**.

---

### 1️⃣ Scope & Responsibilities
#### What This Layer Covers
- Curated visual assets: charts, wordclouds, diagrams, screenshots  
- Final, publishable versions only (clean, named, version-controlled)  
- Normalized naming conventions and storage rules  
- Source mapping: each visual points back to the script that created it
#### What It Does NOT Cover
- Temporary or experimental visuals (stored under `scripts/playground/visuals/`)  
- Raw matplotlib/wordcloud rendering logic  
- Fate Engine or EDA pipeline execution  


### 2️⃣ Directory Layout
visuals/  
├── eda/            → charts, histograms, token maps  
├── fate_engine/    → fate-related visual outputs  
├── wordclouds/     → wordcloud images  
├── architecture/   → diagrams, flows, structural maps  
└── screenshots/    → manual captures (CLI, code, UI)  

All folders contain **only final assets**.


### 3️⃣ Naming Conventions
**Required Format**
```
<category>*<descriptor>*<dataset>.png
```
Examples :
- `eda_token_distribution_hamlet.png`
- `wordcloud_macbeth.png`
- `architecture_pipeline_overview.png`
**Rules**
- lowercase only  
- underscores for readability  
- format : PNG preferred for clarity + transparency  
- no spaces or raw timestamps  


### 4️⃣ Povenance & Traceability
Every visual is traceable to :
1. **The script that produced it**  
2. **The dataset used**  
3. **The version of the pipeline (if relevant)**  

Recommended metadata block inside commit message :
```
[visual] wordcloud_macbeth.png
source: scripts/eda/eda_creatures_03_visuals.py
dataset: data/processed/macbeth_clean.txt
````


### 5️⃣ Usage Examples
#### Load asset in documentation
```md
![Token Distribution](../visuals/eda/eda_token_distribution_hamlet.png)
````
#### Export from Python (recommended workflow)
```python
plt.savefig("visuals/eda/eda_token_distribution_hamlet.png", dpi=300)
```


### 6️⃣ Quality Standards
A visual is considered **publishable** when :
* 1080p minimum
* no overlapping labels
* no debug text
* consistent color palette across visuals
* normalized DPI (typically 300 for charts)


### 7️⃣ Promotion Rules (Playground → Visuals)
A visual is allowed into this folder only when :  
1. Render is stable & replicable
2. Naming follows conventions
3. Source script is referenced
4. No sensitive/local data included


### 8️⃣ Compatibility Notes
* PNG preferred ; SVG allowed for diagrams
* Never commit notebook auto-outputs
* All visuals respect UTF-8 naming & Git-safe characters


### 9️⃣ Glossary
**Asset** : A visual intended for documentation or repo presentation.  
**Provenance** : Metadata explaining where the visual originates.  
**Promotion** : Moving a visual from sandbox → official visuals.


---
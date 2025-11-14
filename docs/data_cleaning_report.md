# data_cleaning_report 

This report documents the **cleaning and structuring processes** applied to **`creators_raw_dataset.csv`**, **`creatures_raw_dataset.md`**, **`dark_stage_raw_dataset.md`** before conversion into final `.csv` files for analysis.  
This process illustrates practical **data wrangling** and **quality assurance** work : ensuring datasets are consistent, readable and ready for further **EDA**, visualizations or integration into analytics pipelines / databases.

---

## 🎭 `creators_raw_dataset.csv`
#### 1️⃣ Initial Audit
- Format : CSV  
- Size : 20 rows  

#### 2️⃣ Cleaning Steps 🗡️ *Purge the impostors*
| Step | Action | Tools / Method |
|------|--------|----------------|
| Data import | Load CSV into pandas DataFrame | `pd.read_csv()` |
| Trim whitespace | Strip extra spaces and newlines | `.str.strip()` |
| Normalize casing | Convert author names to title case | `.str.title()` |
| Standardize categories | Harmonize genre, period, influence columns | Mapping / `.replace()` |
| Remove duplicates | Deduplicate by author_id | `.drop_duplicates()` |
| Reorder data | Sort alphabetically by author name | `.sort_values("author_id")` |
| Save output | Export to `/data/processed/creators_clean.csv` | `.to_csv()` |

#### 3️⃣ Validation
- 
- 
- Cleaned dataset preview saved as `data/metadata/creators_preview.csv`

---

## ✨ `creatures_raw_dataset.md`
#### 1️⃣ Initial Audit
- Format : Markdown table  
- Size : ~150 rows  
- Issues identified :
  - Non-literary entries or “intruders” (irrelevant names, placeholder text)
  - Inconsistent casing and spacing in character names
  - Missing or duplicated entries 
  - Occasional formatting breaks in table delimiters

#### 2️⃣ Cleaning Steps 
| Step | Action | Tools / Method |
|------|--------|----------------|
| Data import | Convert Markdown table to pandas DataFrame | `pd.read_csv(io.StringIO(...), sep="|", skiprows=1)` |
| Trim whitespace | Strip extra spaces and newlines | `.str.strip()` |
| Drop intruders | Keep only legitimate literary characters | Regex / manual curation |
| Normalize casing | Convert to title case | `.str.title()` |
| Remove duplicates | Deduplicate by character name | `.drop_duplicates(subset="character")` |
| Reorder data | Sort alphabetically by character | `.sort_values("character")` |
| Save output | Export to `/data/processed/creatures_clean.csv` | `.to_csv()` |

#### 3️⃣ Validation
✅ Column structure verified  
✅ No missing values  
✅ Alphabetical sorting confirmed  
✅ Cleaned dataset preview saved as `data/metadata/creatures_preview.csv`

---

## 🗣️ `dark_stage_raw_dataset.md`
#### 1️⃣ Initial Audit
- Format : Markdown table  
- Size : ~80 rows (expandable)  

#### 2️⃣ Cleaning Steps 
| Step | Action | Tools / Method |
|------|--------|----------------|
| Data import | Convert Markdown table to pandas DataFrame | `pd.read_csv(io.StringIO(...), sep="|", skiprows=1)` |
| Trim whitespace | Strip extra spaces and newlines | `.str.strip()` |
| Normalize casing | Convert author names & rivalry labels to title case | `.str.title()` |
| Fill missing values | Replace nulls with `None` | `.fillna(value=None)` |
| Standardize categories | Harmonize incident types, intensity & sentiment | Mapping / `.replace()` |
| Remove duplicates | Deduplicate by `author_id`, `incident_type`, `notable_rivalry` | `.drop_duplicates(subset=["author_id","incident_type","notable_rivalry"])` |
| Reorder data | Sort by `author_id` and `incident_type` | `.sort_values(["author_id","incident_type"])` |
| Save output | Export to `/data/processed/dark_stage_clean.csv` | `.to_csv()` |

#### 3️⃣ Validation
- 
- 
- Cleaned dataset preview saved as `data/metadata/dark_stage_preview.csv`

---

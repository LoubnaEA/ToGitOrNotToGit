# data_cleaning_report 

### `creatures_raw_dataset.txt`
Cleaning and structuring process applied to the `creatures.md` dataset before conversion into a `.csv` file for analysis.   
This process illustrates practical **data wrangling** and **quality assurance** work : ensuring datasets are consistent, readable and ready for further EDA or visualization.

#### 1️⃣ Initial Audit
- Format : Markdown table  
- Size : ~150 rows  
- Issues identified :
  - Non-literary entries or “intruders” (irrelevant names, placeholder text)
  - Inconsistent casing and spacing in character names
  - Missing or duplicated entries in key columns
  - Occasional formatting breaks in table delimiters

####  2️⃣ Cleaning Steps 🗡️ *Purge the impostors*
| Step | Action | Tools / Method |
|------|--------|----------------|
| Data import | Convert Markdown table to pandas DataFrame | `pandas.read_csv(io.StringIO(...), sep="|")` |
| Trim whitespace | Strip extra spaces and newlines | `.strip()` |
| Drop intruders | Keep only legitimate literary characters | Regex / manual curation |
| Normalize casing | Convert to title case | `.str.title()` |
| Remove duplicates | Deduplicate by character name | `.drop_duplicates(subset="character")` |
| Reorder data | Sort alphabetically by `character` | `.sort_values("character")` |
| Save output | Export to `/data/processed/creatures_clean.csv` | `.to_csv()` |

#### 3️⃣ Validation
✅ Column structure verified  
✅ No missing values  
✅ Alphabetical sorting confirmed  
✅ Cleaned dataset preview saved as `data/creatures_preview.csv`

---


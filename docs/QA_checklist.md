# ✨ QA_checklist 

This checklist is designed to ensure **quality, consistency, completeness** of the **`creatures.md`** dataset.  
It is structured for **initial population (Shakespeare)** and for **full dataset QA**.  

---

### 1️⃣ Alignment Check, Authors → Creatures

- [ ] All characters are linked to the correct Author_ID in `creators.md`
- [ ] No missing or duplicated Author_IDs
- [ ] Characters only from authors present in the `creators.md` dataset
- [ ] Tier assignment is consistent with author tier (A, B, C)
- [ ] Alphabetical order by character name verified

## 2️⃣ Line Structure, Creature Entry

- [ ] Each row represents **one character**.
- [ ] Core columns present (17 total) :
  - `character`, `author`, `play`, `dramatic_function`, `archetype`, `dominant_traits`, `variables`, `gender`, `social_status`, `human_or_not`, `visual_motifs`, `number_of_characters_in_play`, `role_importance`, `interacts_with`, `speech_length`, `death_status`, `notes`
- [ ] Reserve/advanced columns present (5 total) :
  - `moral_alignment`, `death_status_encoded`, `costume_props`, `introduction_scene`, `gender_performance`
- [ ] No empty mandatory fields in core columns
- [ ] Consistent formatting (capitalization, punctuation, spacing)

### 3️⃣ Character Completeness & Selection

- [ ] Central characters (Protagonist, Villain, Tragic Hero, Revenger) included
- [ ] Semi-central characters (secondary, symbolic) included
- [ ] Marginal, spectral, or symbolic figures added for thematic coverage
- [ ] Archetype coverage complete across dataset
- [ ] Moral alignment assigned where relevant

### 4️⃣ Relational & Contextual QA

- [ ] Interactions (`interacts_with`) are valid and consistent
- [ ] Number of characters in play matches actual play size
- [ ] Role importance reflects narrative weight
- [ ] Speech length is numeric and validated
- [ ] Costume and props information consistent with play and character
- [ ] Introduction scene documented where available
- [ ] Gender performance noted for cross-dressing or disguise

### 5️⃣ Quantitative & Categorical Consistency

- [ ] Categorical columns normalized (`gender`, `social_status`, `dramatic_function`, `archetype`)
- [ ] Numeric columns validated (`speech_length`, `number_of_characters_in_play`)
- [ ] Death status encoded correctly (`0 = alive`, `1 = dead`)
- [ ] Visual motifs emojis correctly applied

### 6️⃣ QA Steps for Shakespeare (Tier A)

- [ ] Populate all main plays (~ 18–20 characters per play)  
- [ ] Verify all character rows adhere to structure  
- [ ] Apply all Core and Reserve columns  
- [ ] Check alignment with `creators.md` (Shakespeare)  
- [ ] Review interactions, role_importance, speech_length  
- [ ] Ensure archetypes and moral alignments are consistent  

### 7️⃣ QA Steps for Full Dataset

- [ ] Repeat Shakespeare QA for all **Tier A** authors  
- [ ] Populate **Tier B** (~ 30–40 characters total), validate all fields  
- [ ] Populate **Tier C** (key characters only), validate all fields  
- [ ] Check total character count (~ 210)  
- [ ] Ensure uniform column structure and formatting across dataset  
- [ ] Cross-check relational integrity : Author_ID → Play_ID → Character_ID  

### 8️⃣ Final Review & Validation

- [ ] Alphabetical sort completed  
- [ ] No duplicates  
- [ ] All missing metadata filled or annotated in `comments`  
- [ ] Dataset ready for EDA, visualization, network analysis  

### Notes
This checklist is **versioned and updated** with each dataset iteration.  



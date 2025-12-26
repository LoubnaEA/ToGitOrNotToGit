# *The Creatures*  

> **Part II - The Jacobean & Elizabethan Edge**  
> Focus : Characters and archetypes, from protagonists to spectral figures, embodying creators’ narrative intentions.  

### ✨ Characters of the English Renaissance Stage

From **1558** to **1642**, the English stage teemed with life, from noble heroes and star-crossed lovers to scheming villains and spectral apparitions.  
These **creatures** are the living embodiments of the playwrights’ moral, political and psychological preoccupations.  

The `creatures.md` dataset constitutes the dramatic counterpart to `creators.md`, focusing on the characters that populate Renaissance drama.  
Each record represents a character entity, structured to balance literary nuance with analytical usability. Each character is catalogued with metadata capturing traits, roles, narrative functions and bridging **literary analysis** with **data exploration**.  
  
- **Number of authors :** 20 core dramatists `creators.md`
- **Estimated total characters :** ~ 210
- **Unit of analysis :** One *creature* (character) per row 
- **Plays covered :** ~ 50–60
- **Characters per play :** 5–15 (up to 20+ in major works)
- **Dataset purpose :** Serve as a pivot between **authors** and **stage personas**, enabling quantitative and qualitative analyses of character, plot, and theatrical archetypes
- **Relational scope :** linked by `Creator_ID`, `Play_ID`, `Character_ID`  

Each creature can thus be traced to its author, play and network of symbolic or emotional relations.

The dataset is designed for both **qualitative interpretation** and **quantitative exploration**.  
A flexible framework adaptable to database, graph, visualization models.

### ✨ Strategy for Dataset Population  

1. **Tiered Author Approach**   
   * **Tier A** 🔴 (Primary authors, major influence) : Jonson, Marlowe, Shakespeare, etc.   
     → Most characters (~ 170–180) come from these authors.  
   * **Tier B** 🟠 (Supporting authors, smaller but significant corpus) : Beaumont, Fletcher, Ford, etc.    
     → ~ 30–40 characters.  
   * **Tier C** 🟡 (Minor or peripheral authors) : Only key characters for coverage (~ 5–10).

2. **Character Selection**   
   * Prioritized **central and semi-central characters** : Protagonist, Villain, Tragic Hero, Revenger.
   * Added **symbolic, marginal and spectral figures** to capture thematic breadth.
   * Ensured coverage of **diverse archetypes** and **moral alignments**.

3. **Data Enrichment**  
   * **Quantitative attributes :** `speech_length`, `role_importance`, `number_of_characters_in_play`  
   * **Qualitative attributes :** `dominant_traits`, `archetype`, `moral_alignment`, `visual_motifs`  
   * **Contextual attributes :** `interacts_with`, `costume_props`, `introduction_scene`, `gender_performance`  

4. **Data Consistency & Validation**  
   * Normalized **categorical columns** (e.g., `gender`, `social_status`, `dramatic_function`).
   * Checked **relational integrity** (`Author_ID` → `Play_ID` → `Character_ID`).
   * Sorted alphabetically and curated manually to remove duplicates, fill missing metadata, ensure consistent formatting.

5. **Analytical Flexibility**  
The dataset is designed to allow both **EDA**, **graph/network analysis** and **visualizations** (e.g., character networks, archetype distributions, gender representation).

### ✨ Creators by Tier

**Tier A 🔴 Core Canon** (4 authors) : Ben **Jonson**, Christopher **Marlowe**, John **Webster**, William **Shakespeare**         
- Deep analyses, rich dataset, major references.       
- These authors represent the most influential voices of the English Renaissance stage, with iconic characters and maximal analytical impact.

**Tier B 🟠 Structuring Pillars** (6 authors) : Francis **Beaumont**, John **Fletcher**, John **Ford**, Thomas **Kyd**, Philip **Massinger**, Thomas **Middleton**    
- Strong depth, solid comparisons, less exhaustive.      
- Key genres such as revenge, tragicomedy and moral tragedy; bridging the Elizabethan and Jacobean periods.   

**Tier C 🟡 Context & Ecosystem** (10 authors) : George **Chapman**, Thomas **Dekker**, Thomas **Heywood**, Robert **Greene**, John **Lyly**, Thomas **Nashe**, John **Marston**, George **Peele**, James **Shirley**, William **Rowley**  
- Minimal coverage, network role, without overloading.     
- Important but heterogeneous voices, often collaborative or fragmentary, providing context and network connections.

### ✨ Columns

#### Core Columns (17)
- **character**, aka Creature, primary identifier of the dramatic persona
- **author**, linked to the corresponding `Author_ID` in `creators.md`    
- **play**, title of the dramatic work in which the character appears (`Play_ID`)   
- **dramatic_function**, (5) structural role in the narrative : 
    - Protagonist, Villain, Transgressor, Outcast / Marginal, Symbolic / Metaphysical Figure 
- **archetype**, (9) dramatic lineage :
    - The Tragic Hero, The Innocent Victim, The Machiavel, The Revenger, The Tempter / Sorcerer, The Fool, The Witch, Death, Fate  
- **dominant_traits**, core moral and psychological attributes, often few in number and highly significant
    - `ambition`, `lust`, `deceit`, `guilt`, etc.      
- **variables**, a broader, dynamic and descriptive list, encompassing various analytical and contextual facets surrounding the character  
    - `ambition`, `revenge`, `betrayal`, etc.
- **gender** : 
  	- Male, Female, Other              
- **social_status** :
  	- Noble, Commoner, Servant, Marginal, Supernatural     
- **human_or_not**, distinguishes mortal from spectral, allegorical or divine entities      
- **visual_motifs**, set of symbolic emojis from the shared legend (🎭👑💀🩸🗡️🔥🕷️…)       
- **number_of_characters_in_play**, contextual density of the dramatic environment                  
- **role_importance**, relative narrative weight
    - Central, Secondary, Chorus, etc.         
- **interacts_with**, primary relational links within the play (characters, factions or pairs)        
- **speech_length**, quantitative indicator of presence                  
- **death_status**, fate of the character :
    - Survives, Dies, Transformed, Unknown
- **notes**

#### Reserve Columns (5)
These columns remain optional or expandable fields for advanced or derived analysis :

- **moral_alignment**, ethical position within the narrative world
    - Virtuous, Ambivalent, Corrupt, etc.
- **death_status**, encoded categorical outcome (e.g. `0=alive`, `1=dead`) 
- **costume_props**, stage appearance and symbolic material culture
- **introduction_scene**, narrative positioning of first entry, for structural mapping and act-based analytics    
- **gender_performance**, cross-dressing, disguise or fluid identity performance

### ✨ Sample from the Cleaned Dataset

The dataset was manually curated and structured, defining relevant columns, ensuring consistent formatting and preparing the data for EDA and visualization.  
Below is a sample from the cleaned `creatures_clean.csv`, produced after data wrangling, validation and alphabetical sorting by character name. The full dataset is available in **data/processed/creatures_clean.csv**

| character        | author               | play                   | dramatic_function    | archetype          | dominant_traits             | variables                          | gender | social_status | human_or_not | visual_motifs           | number_of_characters_in_play | role_importance | interacts_with                 | speech_length | death_status | costume_props        | introduction_scene | gender_performance | moral_alignment | notes                               |
|------------------|----------------------|------------------------|----------------------|--------------------|-----------------------------|------------------------------------|--------|--------------|--------------|-------------------------|-----------------------------|-----------------|-------------------------------|---------------|--------------|----------------------|--------------------|--------------------|------------------|------------------------------------|


---

🎭 `creators.md` → who writes   
✨ `creatures.md` → who acts   
🗣️ `dark_stage.md` → where transgression unfolds   

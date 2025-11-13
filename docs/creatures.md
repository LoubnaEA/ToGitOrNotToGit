# *The Creatures*  

> **Part II - The Jacobean & Elizabethan Edge**  
> Focus : Characters and archetypes, from protagonists to spectral figures, embodying creators’ narrative intentions.  

### ✨ Characters of the English Renaissance Stage

From **1558** to **1642**, the English stage teemed with life, from noble heroes and star-crossed lovers to scheming villains and spectral apparitions.  
These **creatures** are the living embodiments of the playwrights’ moral, political and psychological preoccupations.  

The `creatures.md` dataset constitutes the dramatic counterpart to `creators.md`, focusing on the characters that populate Renaissance drama.  
Each record represents a character entity, structured to balance literary nuance with analytical usability. Each character is catalogued with metadata capturing traits, roles, narrative functions and bridging **literary analysis** with **data exploration**.  
  
- **Number of authors :** 20 core dramatists `creators.md`
- **Estimated total characters :** ~130–150
- **Unit of analysis :** One *creature* (character) per row  
- **Plays covered :** ~50–60
- **Characters per play :** 5–15 (up to 20+ in major works)
- **Dataset purpose :** Serve as a pivot between **authors** and **stage personas**, enabling quantitative and qualitative analyses of character, plot, and theatrical archetypes
- **Relational scope :** linked by `Creator_ID`, `Play_ID`, `Character_ID`  

Each creature can thus be traced to its author, play and network of symbolic or emotional relations.

The dataset is designed for both **qualitative interpretation** and **quantitative exploration**.  
A flexible framework adaptable to database, graph, visualization models.

### ✨ Columns

#### Core Columns (21)
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
- **costume_props**, stage appearance and symbolic material culture
- **introduction_scene**, narrative positioning of first entry, for structural mapping and act-based analytics    
- **gender_performance**, cross-dressing, disguise or fluid identity performance
- **moral_alignment**, ethical position within the narrative world
    - Virtuous, Ambivalent, Corrupt, etc.
- **notes**

#### Reserve Column (1)
This column remain optional or expandable fields for advanced or derived analysis :
 
- **death_status**, encoded categorical outcome (e.g. `0=alive`, `1=dead`) 


### ✨ Sample from the Cleaned Dataset

The dataset was manually curated and structured, defining relevant columns, ensuring consistent formatting and preparing the data for EDA and visualization.  
Below is a sample from the cleaned `creatures_dataset_clean.csv`, produced after data wrangling, validation and alphabetical sorting by character name. The full dataset is available in **data/processed/creatures_dataset_clean.csv**.


| character        | author               | play                   | dramatic_function    | archetype          | dominant_traits             | variables                          | gender | social_status | human_or_not | visual_motifs           | number_of_characters_in_play | role_importance | interacts_with                 | speech_length | death_status | costume_props        | introduction_scene | gender_performance | moral_alignment | notes                               |
|------------------|----------------------|------------------------|----------------------|--------------------|-----------------------------|------------------------------------|--------|--------------|--------------|-------------------------|-----------------------------|-----------------|-------------------------------|---------------|--------------|----------------------|--------------------|--------------------|------------------|------------------------------------|


---

🎭 `creators.md` → who writes   
✨ `creatures.md` → who acts   
🗣️ `dark_stage.md` → where transgression unfolds   

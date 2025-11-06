# *The Creatures*  

### ✨ Characters of the English Renaissance Stage

From **1558 to 1642**, the English stage teemed with life, from noble heroes and star-crossed lovers to scheming villains and spectral apparitions.  
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

#### Core Columns (20)

- **Character**, aka Creature, primary identifier of the dramatic persona
- **Author**, linked to the corresponding `Author_ID` in `creators.md`    
- **Play**, title of the dramatic work in which the character appears (`Play_ID`)   
- **Category / Dramatic Function**, (5) structural role in the narrative : 
    - Protagonist, Villain, Transgressor, Outcast / Marginal, Symbolic / Metaphysical Figure 
- **Archetype / Subtype**, (9) dramatic lineage :
    - The Tragic Hero, The Innocent Victim, The Machiavel, The Revenger, The Tempter / Sorcerer, The Fool, The Witch, Death, Fate  
- **Dominant Traits**, core moral and psychological attributes
    - `ambition`, `lust`, `deceit`, `guilt`, etc.      
- **Variables / Metadata** :
    - `ambition`, `revenge`, `betrayal`, etc.
- **Gender** : 
  	- Male, Female, Other              
- **Social Status** :
  	- Noble, Commoner, Servant, Marginal, Supernatural     
- **Human / Other**, distinguishes mortal from spectral, allegorical or divine entities      
- **Visual Motifs**, set of symbolic emojis from the shared legend (🎭👑💀🩸🗡️🔥🕷️…)       
- **Number of Characters in Play**, contextual density of the dramatic environment                  
- **Role Importance / Stage Time**, relative narrative weight
    - Central, Secondary, Chorus, etc.         
- **Interacts With**, primary relational links within the play (characters, factions or pairs)        
- **Speech Length / Lines Count**, quantitative indicator of presence                  
- **Death Status**, fate of the character :
    - Survives, Dies, Transformed, Unknown
- **Costume Description / Props**, stage appearance and symbolic material culture
- **Introduction Scene / Act**, narrative positioning of first entry
- **Gender Performance**, cross-dressing, disguise or fluid identity performance
- **Moral Alignment**, ethical position within the narrative world
    - Virtuous, Ambivalent, Corrupt, etc.

#### Reserve Columns (5)
These columns remain optional or expandable fields for advanced or derived analysis :

- **Interacts With**, expanded network relationships or graph edges          
- **Speech Length / Lines Count**, detailed metrics (e.g. lines spoken, acts present)     
- **Death Status**, encoded categorical outcome (e.g. `0=alive`, `1=dead`)
- **Costume Description / Props**, for visual analysis or performance studies     
- **Introduction Scene / Act**, for structural mapping and act-based analytics     


### ✨ Dataset

---

`creators.md` → who writes   
`creatures.md` → who acts   
`dark_stage.md` → where transgression unfolds   

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

#### Reserve Columns (3)
These columns remain optional or expandable fields for advanced or derived analysis :

- **interacts_with**, expanded network relationships or graph edges          
- **speech_length**, detailed metrics (e.g. lines spoken, acts present)     
- **death_status**, encoded categorical outcome (e.g. `0=alive`, `1=dead`) 

### ✨ Dataset

| character        | author               | play                   | dramatic_function    | archetype          | dominant_traits             | variables                          | gender | social_status | human_or_not | visual_motifs           | number_of_characters_in_play | role_importance | interacts_with                 | speech_length | death_status | costume_props        | introduction_scene | gender_performance | moral_alignment | notes                               |
|------------------|----------------------|------------------------|----------------------|--------------------|-----------------------------|------------------------------------|--------|--------------|--------------|-------------------------|-----------------------------|-----------------|-------------------------------|---------------|--------------|----------------------|--------------------|--------------------|------------------|------------------------------------|
| Hamlet           | William Shakespeare  | Hamlet                 | protagonist          | tragic_hero        | ambition, indecision        | ambition, fate, betrayal          | male   | noble        | yes          | 🎭🧠💔                 | 25                          | central         | Claudius, Ophelia            | high          | dies         | princely_robe        | act_1_scene_2       | male               | ambivalent       | Prince seeking revenge              |
| Ophelia          | William Shakespeare  | Hamlet                 | innocent_victim      | ingenue            | purity, despair             | virtue, loyalty, madness          | female | noble        | yes          | 💔🕯️🏡                 | 25                          | secondary       | Hamlet, Polonius, Laertes    | medium        | dies         | simple_dress         | act_1_scene_3       | female             | virtuous         | Innocent caught in tragedy          |
| Iago             | William Shakespeare  | Othello                | antagonist           | machiavel          | manipulation, deceit        | manipulation, cunning, power_hunger| male   | commoner     | yes          | 🕷️💀🔥                 | 14                          | central         | Othello, Desdemona          | high          | survives     | dark_cloak           | act_1_scene_1       | male               | corrupt          | Drives chaos, master manipulator     |
| Faustus          | Christopher Marlowe  | Doctor Faustus         | protagonist          | seeker             | curiosity, pride            | knowledge_seeker, hubris           | male   | scholar      | yes          | 🦉🔥👺                 | 23                          | central         | Mephistopheles, Lucifer     | high          | dies         | scholar_robe         | act_1_scene_1       | male               | ambivalent       | Sells soul for knowledge            |
| Mephistopheles   | Christopher Marlowe  | Doctor Faustus         | supernatural_guide   | demon              | cunning, persuasive         | supernatural, temptation           | male   | other        | no           | 👺🔥                    | 23                          | central         | Faustus, Lucifer           | medium        | survives     | demonic_robe         | act_1_scene_3       | male               | corrupt          | Devil guiding Faustus               |
| Viola            | William Shakespeare  | Twelfth Night          | protagonist          | trickster          | intelligence, empathy       | wit, disguise, resilience         | female | noble        | yes          | 🎭🌙❤️                 | 20                          | central         | Orsino, Olivia, Feste      | high          | survives     | page_costume          | act_1_scene_2       | female_disguised    | virtuous         | Cross-dresses as Cesario            |
| Malvolio         | William Shakespeare  | Twelfth Night          | comic_antagonist     | puritan            | pride, self-importance      | discipline, gullibility            | male   | servant      | yes          | 🎩💬                    | 20                          | supporting      | Olivia, Maria, Feste       | medium        | survives     | steward_uniform      | act_1_scene_5       | male               | rigid            | Tricked and humiliated             |
| Hieronimo        | Thomas Kyd           | The Spanish Tragedy    | revenger             | avenger            | sorrow, obsession           | bereavement, justice               | male   | noble        | yes          | 🗡️💀                    | 16                          | central         | Isabella, Lorenzo          | high          | dies         | mourning_garments    | act_1_scene_1       | male               | ambivalent       | Consumed by vengeance             |
| Barabas          | Christopher Marlowe  | The Jew of Malta       | antihero             | outsider           | cunning, greed              | outsider, vengeance                | male   | merchant     | yes          | 💰👺                    | 28                          | central         | Abigail, Ferneze, Ithamore | high          | dies         | merchant_robe        | act_1_scene_1       | male               | corrupt          | Manipulates and deceives          |
| Lady Macbeth     | William Shakespeare  | Macbeth                | catalyst             | manipulator        | ambition, ruthlessness      | ambition, guilt                   | female | noble        | yes          | 👑🩸                    | 15                          | central         | Macbeth                   | medium        | dies         | nightgown_crown      | act_1_scene_5       | female             | corrupt          | Incites murder                  |
| Macbeth          | William Shakespeare  | Macbeth                | protagonist          | tragic_hero        | ambition, madness           | ambition, fate, guilt             | male   | noble        | yes          | 👑🩸💀                   | 15                          | central         | Lady Macbeth               | high          | dies         | royal_costume        | act_1_scene_3       | male               | corrupt          | Scottish king driven by prophecy     |
| Desdemona        | William Shakespeare  | Othello                | innocent_victim      | tragic_heroine      | loyalty, love, innocence    | loyalty, love, betrayal           | female | noble        | yes          | 💔❤️                    | 14                          | secondary       | Othello                   | medium        | dies         | noble_dress          | act_1_scene_3       | female             | virtuous         | Faithful wife wrongfully accused    |
| Romeo            | William Shakespeare  | Romeo and Juliet       | protagonist          | tragic_hero        | passionate, impulsive       | love, fate, rebellion             | male   | noble        | yes          | 💔🔥                    | 20                          | central         | Juliet                    | high          | dies         | noble_costume        | act_1_scene_1       | male               | virtuous         | Hopeless romantic               |
| Juliet           | William Shakespeare  | Romeo and Juliet       | protagonist          | tragic_heroine     | passionate, brave           | love, fate                     | female | noble        | yes          | 💔🔥                    | 20                          | central         | Romeo                     | high          | dies         | noble_dress          | act_1_scene_1       | female             | virtuous         | Young lover defying family feud     |
| Falstaff         | William Shakespeare  | Henry IV               | comic_relief         | jovial_brawler     | wit, cowardice             | wit, drinking, cowardice          | male   | noble        | yes          | 💬🎭                    | 18                          | supporting      | Prince Hal                | medium        | survives     | soldier_armor        | act_1_scene_2       | male               | flawed            | Merry knight and trickster        |
| Prince Hal       | William Shakespeare  | Henry IV               | protagonist          | heir               | reckless, growing          | growth, redemption               | male   | royal        | yes          | 👑🎭                    | 18                          | central         | Falstaff                  | high          | survives     | royal_armor          | act_1_scene_1       | male               | ambivalent       | Future king on path to maturity     |
| Hotspur          | William Shakespeare  | Henry IV               | antagonist           | foil               | fiery, honor-bound          | rebellion, honor                | male   | noble        | yes          | 🗡️🔥                    | 18                          | antagonist     | Prince Hal                | medium        | dies         | knight_armor         | act_1_scene_2       | male               | virtuous         | Hotheaded nobleman opposing Prince Hal |
| Isabella         | Thomas Kyd           | The Spanish Tragedy    | innocent_victim      | pure               | loyalty, sorrow             | loyalty, virtue               | female | noble        | yes          | ⚖️🩸                    | 16                          | secondary       | Hieronimo                | medium        | dies         | mourning_dress       | act_1_scene_3       | female             | virtuous         | Sister avenging brother             |
| Ferneze          | Christopher Marlowe  | The Jew of Malta       | foil                 | nobleman            | justice, honor             | justice, revenge             | male   | noble        | yes          | ⚖️🗡️                    | 28                          | secondary       | Barabas                  | medium        | survives     | noble_armor          | act_1_scene_4       | male               | virtuous         | Opposes Barabas                  |
| Octavius Caesar  | William Shakespeare  | Julius Caesar          | leader               | ruler              | pragmatic, honorable        | power, loyalty               | male   | noble        | yes          | 👑⚖️                    | 15                          | central         | Antony                   | high          | survives     | general_uniform      | act_1_scene_1       | male               | virtuous         | Roman ruler and military leader      |
| Brutus           | William Shakespeare  | Julius Caesar          | protagonist          | tragic_hero        | honor, betrayal             | loyalty, honor, guilt        | male   | noble        | yes          | ⚖️🗡️💀                  | 15                          | central         | Caesar                   | high          | dies         | senator_robe         | act_1_scene_1       | male               | virtuous         | Assassin struggling with conscience  |
| Lady Percy       | William Shakespeare  | Henry IV               | supporting           | loyal_wife          | pride, devotion             | loyalty, sorrow              | female | noble        | yes          | ❤️🏡                    | 18                          | minor           | Hotspur                  | low           | survives     | noble_dress          | act_1_scene_1       | female             | virtuous         | Wife of Hotspur, loyal and proud     |
| Puck             | William Shakespeare  | A Midsummer Night’s Dream | trickster         | fairy               | mischievous, playful        | magic, mischief              | male   | other        | no           | 🌙🪞🔥                    | 14                          | supporting      | Oberon                   | medium        | survives     | fairy_costume         | act_1_scene_1       | male               | neutral          | Magical sprite causing havoc         |
| Oberon           | William Shakespeare  | A Midsummer Night’s Dream | supernatural_guide | king_of_fairies     | power, mischief             | magic, power                | male   | other        | no           | 👑🔥                    | 14                          | supporting      | Titania                  | medium        | survives     | fairy_robes           | act_1_scene_1       | male               | neutral          | King of the fairies               |
| Titania          | William Shakespeare  | A Midsummer Night’s Dream | supernatural_guide | queen_of_fairies    | pride, jealousy             | magic, romance              | female | other        | no           | 👑🔥💔                   | 14                          | supporting      | Oberon                   | medium        | survives     | fairy_dress           | act_1_scene_1       | female             | neutral          | Queen of the fairies               |


---

🎭 `creators.md` → who writes   
✨ `creatures.md` → who acts   
🗣️ `dark_stage.md` → where transgression unfolds   

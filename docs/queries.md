# *Narrative Queries*

> **Part IV - Digital Afterlife**  
> Focus : Exploratory and analytical queries linking `creators.md`, `creatures.md` and `dark_stage.md` incidents ; network, temporal and comparative analysis.

### 🛋️ Have a sit

This document lists **exploratory and analytical queries** for the three core datasets (`creators.md`, `creatures.md`, `dark_stage.md`).    
Queries link **authors, characters and offstage intrigues**, supporting **literary analysis, network mapping and visualization**.  

Each query can be implemented in **SQL, Python (Pandas) or graph databases (Neo4j)**.  
`stage_mood` and `visual_motifs` serve as **quantitative proxies for narrative tone and social sentiment**, enabling **qualitative interpretation** and **data-driven insights**.  

Whether exploring character networks, temporal trends or scandalous anecdotes, these queries turn the stage into a **data playground**.


### 🛋️ Queries, Relationships, Exploration Angles

#### Creators → Creatures   
* Map authors to their characters and archetypes  
* Compare creators’ thematic preferences and stage motifs  
#### Creatures → Dark Stage  
* Identify characters involved in offstage incidents  
* Correlate character traits with backstage feuds  
#### Cross-Period Analysis  
* Examine historical and stylistic evolution across Elizabethan, Jacobean and Caroline eras   
#### Sentiment Mapping  
* Analyze emotional tone, gossip sentiment, mood transitions through `stage_mood`   


### 🛋️ Query Catalogue

#### **Authors & Works**
1. Nber of plays per author
2. All plays censored or politically controversial
3. Genre distribution by period (Elizabethan vs Jacobean)
4. List of collaborative plays and co-authors
5. Authors active across multiple genres
6. Authors with highest nber of surviving works
7. Average nber of characters per play per author

#### **Characters & Traits**
8. Count protagonists, villains, transgressors, symbolic figures
9. Identify characters marked by `ambition` or `revenge`
10. Map `interacts_with` networks per play
11. Detect characters appearing in multiple plays
12. Most common archetypes by period
13. Characters associated with multiple visual motifs
14. Trait prevalence comparison (`deceit`, `lust`, `guilt`) by era
15. List characters of `marginal` or `supernatural` status

#### **Stage & Plot Dynamics**
16. Speech length distribution by character
17. Mortality rate by category (protagonist, villain, etc.)
18. 1st appearance by act and scene
19. Stage importance vs nber of lines spoken
20. Characters central to multiple plotlines
21. Patterns of deaths, survival and transformations
22. Timing of revenge acts within plays

#### **Visual & Symbolic Motifs**
23. Frequency of visual motifs (🎭👑💀🔥…)
24. Co-occurrence of motifs with archetypes
25. Motif usage comparison across Elizabethan and Jacobean plays
26. Plays with highest motif density
27. Recurring motif combinations among villains or transgressors
28. Evolution of symbolic motifs over decades

#### **Dark Stage / Gossip & Scandals**
29. Nber of offstage incidents per author
30. Incidents per play involving a character
31. Most frequent `stage_mood` emojis (😏😡🤫🥰…)
32. Sentiment distribution (`jealousy`, `envy`, `admiration`, `humiliation`)
33. Recurring author collaborations or rivalries
34. Incidents linking authors and their creatures
35. Scandal frequency by period or location
36. Incidents leading to censorship or suppression

#### **Cross-Dataset Analysis**
37. Characters appearing in multiple incidents
38. Authors with highest scandal-to-play ratio
39. Correlation between character traits and `stage_mood`
40. Characters central to offstage social networks
41. Influence of offstage feuds on character portrayal
42. Motif use in scandal-related vs neutral plays
43. Links between narrative archetypes and real-world rivalries

#### **Temporal & Comparative Queries**
44. Average nber of tragic deaths per decade
45. Frequency of motifs per decade
46. Incidents by historical year or context
47. Archetype prevalence comparison across periods
48. Correlation between political events and offstage incidents
49. Sentiment (`stage_mood`) changes over time
50. Shifts in narrative focus (protagonists vs villains) per period

---

🪑 *Query of the Unseen Observer*
```sql 
SELECT *
FROM stage
WHERE seat = 'C4' AND occupant IS NULL;
```

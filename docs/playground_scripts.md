# playground_scripts

Project **playground scripts** repository overview.  
Each script is a small experiment or demonstration related to Shakespeare, Python and  Git.  
Use this guide to understand each script's purpose, inputs and outputs.

Requires Python packages : `matplotlib`, `numpy`, `pillow`, `wordcloud`

---

## [Shakespearean Fate](#shakespearean-fate)
**Path :** `scripts/playground/shakespearean_fate.py`    
A whimsical script that outputs a Shakespeare-style warning based on your code commits or features.  
**Ex :**
```text
Push not tonight, for the linter’s wrath shall smite thee.  
````

## [Python Omens](#python-omens)
**Path :** `scripts/playground/python_omens.py`  
This script provides Python-related warnings or omens, e.g., about versions, dependencies, environment issues.  
**Ex :**  
```text
A cursed dependency lies dormant in thy environment.txt—update or be doomed.
```

## [Git Whisperer](#git-whisperer)
**Path :** `scripts/playground/git_whisperer.py`  
Outputs warnings about Git repository state, uncommitted changes, potential merge conflicts.  
**Ex :** 
```text
Your branch 'main' bleeds with uncommitted changes. The shadows urge : commit, or face chaos. Merge conflicts brew like storm clouds.
```

## [Runner Prophecy](#runner-prophecy)
**Path :** `scripts/playground/runner_prophecy.py`  
A runner script that executes all playground scripts in one go and aggregates their messages.  
**Ex Output :**  
```text
🕯️  THE PROPHETIC SCROLL OF CODE & COMMITS  🕯️

------------------------------------------------------------------------
⏳ Shakespearean Fate :
Beware the feature flag, for it hideth serpents beneath its cloak.
------------------------------------------------------------------------
🐍 Pythonic Omen :
The Python spirits whisper: version 3.11 is fickle on Windows. Beware incompatible wheels.
------------------------------------------------------------------------
🌑 Git Whisper :
Your branch 'main' bleeds with uncommitted changes. The shadows urgec: commit, or face chaos. Your commit history hides a secret regret.
------------------------------------------------------------------------
End of scroll.
```

## [Shakespeare WordCloud](#shakespeare-wordcloud)
**Path :** `scripts/playground/shakespeare_wordcloud.py`   
Generates word clouds from Shakespeare texts (`hamlet.txt`, `macbeth.txt`, `romeo_and_juliet.txt`) located in `data/raw/playground/`   
![wordcloud_hamlet](scripts/playground/visuals/wordcloud_hamlet.png)   
![wordcloud_macbeth](scripts/playground/visuals/wordcloud_macbeth.png)   
![wordcloud_romeo_and_juliet](scripts/playground/visuals/wordcloud_romeo_and_juliet.png)   
![wordcloud_screenshot](scripts/playground/visuals/wordcloud_screenshot.png)   

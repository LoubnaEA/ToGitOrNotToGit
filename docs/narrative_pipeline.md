# 🏰 narrative_pipeline  

This document explains the flow of narrative artifacts through the Fate Engine, from generation to runtime outputs.  
Narrative content is produced through a deterministic-yet-playful pipeline.

---

## 🧩 `scripts/artifacts/`
Contains all narrative artifacts, each defining outcomes, categories, and contextual triggers.
Artifacts are the source of truth for the Fate Engine runtime and QA tests.
Each artifact is an atomic narrative generator exposing a `generate()` function
that returns one or more outcomes.

🏹 `duchess.py`, `euphues.py`, **`faustus.py`**, `hamlet.py`, `macbeth.py`, `ophelia.py`,  `random_fate.py`, `spanish_tragedy.py`   

**Manifest** : `data/metadata/artifacts_manifest.json`  
**Integration** : loaded by Fate Engine via `load_artifact()`  

**Ex** : artifacts/**`faustus.py`**
```python
"""Moral downfall through forbidden knowledge"""

import random

def generate():
    outcomes = [
        "💀 Faustus loses himself to the pact (damnation inevitable)",
        "💀 Bargain unravels; soul claimed",
        "🌿 Temporary reprieve, but fate sealed"
    ]
    return [random.choice(outcomes)]
```

##  Fate Engine Core 🔮 `scripts/fate_engine/`  
Generates outcomes and “prophecies” based on artifacts and inputs.  
Responsible for narrative logic, deterministic or branching.
The engine does not run on its own ; it is always called by runtime scripts.

**Core scripts** :  
- **`prophecy_generator.py`** → generates narrative outcomes  
- `text_parser.py` → text utilities for narrative processing  
- `visual_helper.py` → visual support for outputs  

**Runtime** : called by `run_fate_engine.py` in playground  

**Ex** : **`prophecy_generator.py`**
```python
PROPHECIES = [...]
def generate_prophecy(character=None):
```

## 🎪 `scripts/playground/` 
Where the engine is executed and tested. Supports experimentation and orchestration.  

**Key scripts** :  
 
- `git_whisperer.py` → generates artifacts from Git history  
- `python_omens.py` → detects omens in text or code
- `run_fate_engine.py` → main execution script
- `runner_prophecy.py` → orchestrates artifacts & prophecy generator  
- `shakespeare_wordcloud.py` → generates word clouds from Shakespeare texts
- `shakespearean_fate.py` → narrative helper functions
- `test_artifacts_loader.py` → validates artifacts and manifest consistency

**Artifacts runtime** : can call `run_artifacts.py` to process multiple artifacts  


## Utility `scripts/` 🛠️
Supporting scripts that facilitate workflow but do not generate narrative outputs.
  
**Ex** : `md_to_delim.py` → converts markdown to delimited formats  
**Ex** : `test_run_all.py` → runs tests across scripts  


## Outputs 🕊️ `visuals/fate_outputs/`, `visuals/screenshots/`, `visuals/wordclouds/`  
Contains all results of the narrative pipeline, including :  
- Generated prophecy texts  
- Word clouds and visual summaries  
- Screenshots of runs and charts  

These outputs can be referenced in documentation or presentations.

## Flow Summary
🧩 Artifacts  → 🔮 Fate Engine  → 🎪 Playground (runtime scripts & tests) → 🛠️ Utilities → 🕊️ Outputs

# 🏰 narrative_pipeline  

This document explains the flow of narrative data and scripts, from artifacts to runtime outputs.   

---

## 🧩 `scripts/artifacts/`
Contains all narrative artifacts, each with defined outcomes, categories, and contextual triggers.  
These are the source of truth for the Fate Engine runtime and QA tests.

**Ex** : `hamlet.py`, `macbeth.py`, `ophelia.py`, `spanish_tragedy.py`  
**Ex** : `artifacts_manifest.json` in `data/metadata/`  

**Integration** : loaded by Fate Engine via `load_artifact()`  

## 🔮 `scripts/fate_engine/`  
Generates outcomes and “prophecies” based on artifacts and inputs.  
Responsible for narrative logic, deterministic or branching.

**Core scripts** :  
- `prophecy_generator.py` → generates narrative outcomes  
- `text_parser.py` → text utilities for narrative processing  
- `visual_helper.py` → visual support for outputs  

**Runtime** : called by `run_fate_engine.py` in playground  

## 🎪 `scripts/playground/` 
Where the engine is executed and tested. Supports experimentation and orchestration.  

**Key scripts** :  
- `run_fate_engine.py` → main execution script  
- `runner_prophecy.py` → orchestrates artifacts & prophecy generator  
- `shakespearean_fate.py` → narrative helper functions  
- `python_omens.py` → detects omens in text or code  
- `git_whisperer.py` → generates artifacts from Git history  

**Artifacts runtime** : can call `run_artifacts.py` to process multiple artifacts  

## Utility `scripts/` 🛠️
Supporting scripts that don’t directly generate output but facilitate the workflow.  
  
**Ex** : `md_to_delim.py` → converts markdown to delimited formats  
**Ex** : `test_run_all.py` → runs tests across scripts  

## Outputs 🕊️ `visuals/fate_outputs/`, `visuals/screenshots/`, `visuals/wordclouds/`  
Contains all results of the narrative pipeline, including :  
- Generated prophecy texts  
- Word clouds and visual summaries  
- Screenshots of runs and charts  

**Tip** : these outputs can be directly referenced in documentation or presentations.  

## Flow Summary
🧩 Artifacts  → 🔮 Fate Engine  → 🎪 Playground (runtime & tests) → 🛠️ Utilities → 🕊️ Outputs



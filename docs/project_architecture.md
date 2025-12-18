# 🧭 project_architecture  

This document provides a **clear, high-level view of the `ToGitOrNotToGit 💀` ecosystem**.  
The repository can be read as a **layered system**, where narrative, data, code and validation interact.

---

## Conceptual Layers
**`ToGitOrNotToGit 💀`** is structured around four main layers. Each folder belongs primarily to one of these layers, while still interacting with the others.

> **Act I : The Shakespearean Death Map**    
* **Source Material & Data** : the literary corpus and its transformations   
> **Act II : Jacobean & Elizabethan Edge**   
* **Analysis & Exploration** : EDA, notebooks, scripts   
> **Act III : Mapping the Taboo**   
* **Validation & Quality** : schemas, tests, QA logic   
> **Act IV : Digital Afterlife**   
* **Narrative & Outputs** : documentation, visualizations, published artifacts  

## Repository Tree (Simplified)
```
ToGitOrNotToGit 💀 /
│
├── 📁 data/        → datasets and metadata
├── 📁 docs/        → narrative documentation and published HTML
├── 📁 features/    → BDD-style feature files describing scenarios and expected behaviors
├── 📁 notebooks/   → exploratory Jupyter notebooks (clean, no outputs)
├── 📁 references/  → external sources and research material
├── 📁 scripts/     → data processing, analysis, creative engines
├── 📁 security/    → thematic placeholders (plague, corruption, risk)
├── 📁 tests/       → automated tests and QA scenarios
├── 📁 visuals/     → generated images, screenshots, text outputs
│
├── README.md
├── requirements.txt
└── pytest.ini
```

This structure reflects a **data-first but narrative-driven workflow**.

## Data Layer (`📁 data/`)
This directory keeps raw datasets separate from validated and processed ones, following standard data engineering practices and ensuring traceability.  

* `raw/` Original or lightly transformed sources (texts, extracted tables, drafts)  
* `processed/` Cleaned, normalized datasets ready for analysis or testing   
* `metadata/` Schemas, validation rules, and structural definitions used for QA-style checks   

## Analysis Layer (`📁 notebooks/` & `📁 scripts/eda/`)

### Notebooks
* Jupyter notebooks used for **exploratory data analysis**
* Outputs are cleared before commit
* HTML exports are published via GitHub Pages (see `docs/`)

### EDA Scripts
* Python scripts that formalize exploratory steps
* Statistical summaries, cleaning logic, quality checks
* Designed to be reproducible and testable

## Validation & QA Layer (`📁 tests/`, `📁 features/`, `📁 data/metadata/`)
This project borrows heavily from **software QA practices** :  

* JSON schemas and validation files define expected structures
* Pytest tests validate logic, transformations and pipelines
* Gherkin-style feature files express narrative test scenarios

The idea is to treat literary data as **systems that can fail** and therefore must be tested.

## Narrative & Documentation Layer (`📁 docs/`)
This layer connects technical work to interpretation and storytelling, serving as the main interface for readers.  

* conceptual explanations
* dataset descriptions
* cleaning reports
* published EDA notebooks in HTML format

## Visual & Generated Outputs (`📁 visuals/`)
This directory gathers outputs and represents the **visible trace of the system in action**.  

* generated text outputs
* word clouds
* screenshots of executions
* visual artifacts used in analysis or presentation

## How to Read the Project
➡️ Suggested entry points :  

* **`README.md`** → Conceptual overview  
* **`📁 docs/`** Narrative and results  
* **`📁 notebooks/`** Exploratory reasoning  
* **`📁 scripts/`** Implementation details  
* **`📁 tests/`** Validation and QA logic  

## Current State
The repository reflects an **organic, research-driven evolution**.  
Some areas are exploratory by design, others already stabilized.  

This document serves as a reference point.

---

*`architecture_stability`* : assumed  
*`entropy_level`* : rising  🌑

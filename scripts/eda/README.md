# EDA Subsystem

> The EDA layer describes *what exists in the text*, without interpreting *what it means*.

This subsystem provides all **deterministic analytical primitives** used to explore, decompose and quantify narrative text datasets.  
It serves as the **foundation layer** for understanding textual structure and distributions before any narrative interpretation or fate logic is applied.  

---

### 1️⃣ Scope & Responsibilities

**What this layer does**
* **Text decomposition**
  * sentences
  * paragraphs
  * high-level structural units
* **Token and n-gram analysis**
  * token frequencies
  * global and segment-level statistics
* **Analytical feature extraction**
  * quantitative signals derived from text
* **Visualization preparation**
  * normalized data structures for charts and wordclouds

This layer answers the question : *What is objectively present in the text ?*

**What this layer does NOT do**
* No fate evaluation
* No narrative decision logic
* No scoring, ranking or interpretation
* No persistence (handled elsewhere)
* No ML or probabilistic modeling

EDA is **descriptive**, never prescriptive.

### 2️⃣ Directory Layout
```
scripts/eda/
├── token_stats.py     → token frequencies, n-grams, counts
├── structures.py      → structural segmentation & hierarchy
├── visual_prep.py     → visualization-ready data structures
└── examples/          → small reference outputs (dev/debug)
```

### 3️⃣ Data Contracts

**Input**
* `str` (raw text)
* `list[str]` (pre-split segments)
* Tokenized input is accepted where explicitly documented
  
**Output**  
Always returns **pure Python analytical structures**  
(no side effects, no IO, no global state).  

Ex :
```python
{
  "tokens": {"the": 523, "king": 41},
  "ngrams": {"to_be": 18},
  "structure": {
    "sentences": 123,
    "paragraphs": 14
  }
}
```

### 4️⃣ Determinism Guarantees

This layer is **fully deterministic** :
* Same input text → same output
* Same tokenizer rules → identical results
* No randomness
* No seeding required

This guarantees :
* reproducibility
* test stability
* QA-friendly behavior

### 5️⃣ Usage Examples

**Token Frequencies**
```python
from eda.token_stats import compute_frequencies

freqs = compute_frequencies("To be, or not to be.")
```
**Structural Analysis**
```python
from eda.structures import analyze_structure

info = analyze_structure(text)
```
**Visualization Preparation**
```python
from eda.visual_prep import prep_wordcloud_data

wc_data = prep_wordcloud_data(freqs)
```

### 6️⃣ Testing & Validation

All EDA primitives are covered by unit tests.

Validation includes :
* frequency correctness
* structural integrity
* output shape consistency
* regression stability

Run tests :
```bash
pytest -q scripts/eda
```

### 7️⃣ Relationship to Other Layers

**Feeds** :
  * Fate Engine
  * narrative artifacts (indirectly)
  * exploratory notebooks

**Does not depend on** :
  * artifacts layer
  * runtime scripts
  * scoring logic

EDA is intentionally **downstream-agnostic**.

### 8️⃣ Future Extensions (Planned)

**This layer is designed to evolve toward** :  
* richer structural models (acts, scenes, speakers)
* symbolic density metrics
* emotion / motif frequency layers
* artifact-backed EDA persistence
* cross-text comparative analysis
* dataset-level aggregation

**Future versions may expose** :  
* reusable EDA snapshots
* schema-validated analytical outputs
* API-friendly EDA endpoints

### 9️⃣ Compatibility Notes
* Python ≥ 3.10
* UTF-8 normalized text processing
* Standard library only (no external NLP dependencies)

### 1️⃣0️⃣ Glossary
**EDA Layer**  
Deterministic analytical view of a text.  
**Feature**  
A quantitative signal derived from raw text.  
**Structure**  
Logical decomposition of narrative text.  
**Determinism**  
Identical inputs always produce identical outputs.  


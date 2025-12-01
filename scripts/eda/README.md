# EDA Subsystem

Provides all analytical primitives required to explore, quantify and decompose text datasets.  
Functions here power data understanding, feature derivation, visual preparation used by other modules.

---

### 1. Responsibilities
#### Core Capabilities
- Token frequency computation (global + per-segment)
- Structural decomposition (sentences, paragraphs, acts)
- Statistical preparation for EDA visualizations
- Feature builders for downstream modules (Fate Engine, models, etc.)
#### Explicit Non-Goals
- No fate scoring  
- No heavy ML modeling  
- No persistent storage (handled by `artifacts/`)  


### 2. Directory Layout
scripts/eda/  
├── token_stats.py     → n-grams, frequencies, TF maps  
├── structures.py      → structural segmentation + hierarchy  
├── visual_prep.py     → data prep for charts/wordclouds  
└── examples/          → small sample outputs for debugging  


### 3. Data Flow & Contracts
#### Input Contract
`str` or list of strings (tokenized text accepted).
#### Output Contract
Always returns a **pure analytical structure**, e.g. :
```json
{
  "tokens": { "the": 523, "king": 41 },
  "structure": {
      "sentences": 123,
      "paragraphs": 14
  },
  "ngrams": { "to_be": 18 }
}
````
#### Deterministic Guarantees
* Same text → same frequencies
* Same tokenizer settings → identical EDA layers
* No randomness ; fully reproducible


### 4. Usage Examples
#### Token Frequencies
```python
from eda.token_stats import compute_frequencies
freqs = compute_frequencies("To be, or not to be.")
```
#### Structural Decomposition
```python
from eda.structures import analyze_structure
info = analyze_structure(text)
```
#### Visual Prep
```python
from eda.visual_prep import prep_wordcloud_data
wc_data = prep_wordcloud_data(freqs)
```


### 5. Error Model
| Code   | Error Type             | Trigger                     |
| ------ | ---------------------- | --------------------------- |
| EDA-01 | InvalidInputError      | Non-string or empty input   |
| EDA-02 | TokenizationError      | Failure during segmentation |
| EDA-03 | StatsComputationError  | Bad intermediate state      |
| EDA-04 | VisualizationPrepError | Data shape mismatch         |


### 6. Test Execution
```bash
pytest -q scripts/eda
```
Coverage includes :
* Token stats correctness
* Structural integrity checks
* Wordcloud/chart prep outputs


### 7. Promotion Rules
A new EDA feature becomes stable when :
1. Outputs are deterministic
2. It is used by ≥1 other module
3. Schema remains backward compatible
4. Tests cover frequency, structure and shape checks


### 8. Compatibility Notes
* Python ≥ 3.10
* UTF-8 normalized processing
* Tokenization is dependency-free (standard library only)


### 9. Glossary
**EDA Layer** : Analytical map/layer describing text.  
**Feature Builder** : EDA output feeding a downstream system.  
**Segmentation** : Splitting text into meaningful structural blocks.  


---

# Dev Sandbox - Playground Scripts

The playground provides an **isolated development space** for experimentation, prototypes, non-production logic.  
Its purpose is to accelerate iteration while keeping the main codebase clean, stable and maintainable.

This zone **must never affect** the production-ready modules (`fate_engine/`, `eda/`, `artifacts/`).

---

### 1. Scope & Responsibilities

#### What the Playground Is For
- Quick experiments  
- Draft EDA exploration  
- Temporary visualization tests  
- One-off transformations  
- Debug utilities  
- Inline experiments for future modules  
#### What It Is NOT For
- Final visuals  
- Production-ready logic  
- Stable APIs or public functions  
- Long-term scripts without owners  


### 2. Directory Layout (Recommended)
scripts/playground/  
├── notebooks/         → scratch notebooks (optional)  
├── visuals/           → disposable charts (gitignored)  
├── scratch/           → ideas, prototypes, temp code  
└── utils/             → optional small helpers for sandbox only  

`visuals/` is protected by a `.gitignore` to prevent accidental commits.


### 3. Promotion Lifecycle  
A script follows a clear **Dev → Candidate → Stable** path.  

- **Stage 1 : Dev** (default)
  - Located in `scripts/playground/`
  - Rapid iteration, incomplete logic
  - No tests required  

- **Stage 2 : Candidate**  
Moved to the target module (e.g. `scripts/eda/`)  
Criteria :
  - Code is coherent, reusable, and documented
  - Output is deterministic
  - Naming + folder choice validated

- **Stage 3 : Stable**  
Becomes part of the official codebase when :
  - Tests exist  
  - Public function signatures are clean  
  - No debug or print statements  
  - Follow module conventions (EDA/Fate/Artifacts)  


### 4. Cleanup Policies
**Weekly Cleanup (recommended)**
Remove :
- orphan scripts  
- duplicated logic  
- unused visual outputs  
- stale notebooks  
- heavy scratch files  

**Commit Rules**
- Never commit large experimental outputs  
- Always document promotions (`playground → module`) in commit messages  


### 5. Usage Example
**Quick Prototype**
```python
# scripts/playground/scratch/creature_test.py
from scripts.eda.token_stats import compute_frequencies
freqs = compute_frequencies(open("data/raw/hamlet.txt").read())
print(freqs["king"])
````
**Visual Temporary Export**
```python
plt.savefig("scripts/playground/visuals/test_plot.png", dpi=120)
```

### 6. Integration with the Repo
The playground is designed for :
* fast iteration
* safe experimentation
* low coupling with the main architecture

Modules in `scripts/` **may depend on playground prototypes**,
but nothing in the playground should depend on stable modules.


### 7. Compatibility Notes
* Python ≥ 3.10
* No external dependencies required
* All sandbox code must remain isolated from CI/CD


### 8. Glossary
**Playground** : Experimental zone with no stability guarantees.  
**Promotion** : Migration of a script from sandbox → official module.  
**Candidate** : Script pending validation before entering stable modules.  

---


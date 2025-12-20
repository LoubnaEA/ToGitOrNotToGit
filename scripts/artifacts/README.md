# Narrative Artifacts Layer

> Artifacts are small, testable narrative building blocks that power the Fate Engine. 

This directory contains all **narrative artifacts** used by the Fate Engine.
Artifacts are small, self-contained Python modules that generate deterministic or contextual narrative outcomes.

They represent the **atomic narrative units** of the project.

---

## 1️⃣ Scope & Responsibilities

**What artifacts are**
* **Atomic narrative generators**
* Each artifact exposes a `generate()` function
* Returns one or more **narrative outcomes**
* Outcomes may be :
  * deterministic
  * conditional
  * seeded / reproducible
* Artifacts are :
  * human-readable
  * testable
  * executable in isolation

Artifacts are the **source of truth** for :
* narrative behavior
* QA validation
* future API exposure

**What artifacts are NOT**
* No orchestration logic
* No runtime execution flow
* No visualization logic
* No Fate Engine control logic

Artifacts **describe narratives**, they do not decide *when* or *how* they run.

### 2️⃣ Directory Layout
```
scripts/artifacts/
├── duchess.py
├── euphues.py
├── faustus.py
├── hamlet.py
├── macbeth.py
├── ophelia.py
├── random_fate.py
├── spanish_tragedy.py
└── __init__.py
```

Metadata and validation schemas live in :

```
data/metadata/
├── artifacts_manifest.json
├── creators_schema.json
└── creators_validation.json
```

### 3️⃣ Artifact Contract

Each artifact must :
* Be discoverable by the runtime
* Expose a public `generate()` function
* Return :
  * a list of outcomes, or
  * a structured outcome object
* Match its declaration in `artifacts_manifest.json`

**Minimal example**
```python
def generate():
    return ["💀 Fate is sealed"]
```

### 4️⃣ Execution & Runtime Usage

Artifacts are **not executed directly**.

They are called via :
* `scripts/run_artifacts.py` (smoke test / demo)
* `scripts/playground/runner_prophecy.py`
* Fate Engine runtime scripts

Ex (runtime) :
```bash
python -m scripts.run_artifacts
```

### 5️⃣ Testing & Validation

Artifacts are fully testable and covered by automated checks.

Validation includes :
* artifact discovery
* manifest consistency
* outcome structure validation
* runtime execution without errors

See **`tests/README.md`** for full testing strategy.

### 6️⃣ Determinism & Levels

Some artifacts reference **levels** (e.g. max level 7).

These represent :
* narrative escalation thresholds
* stress / corruption / revenge intensity
* bounded deterministic ranges used for testing and reproducibility

They are **domain-level narrative controls**, not technical constraints.

### 7️⃣ Future Extensions (Planned)

This layer is intentionally simple but designed to evolve toward :
* branching artifacts
* parameterized outcomes
* external artifact loading
* API-based artifact retrieval
* artifact persistence & versioning
* contract-based artifact schemas

Current artifacts are **pure Python**, future versions may support :
* JSON-defined artifacts
* database-backed artifacts
* LLM-augmented narratives

### 8️⃣ Compatibility Notes
* Python ≥ 3.10
* Artifacts are deterministic when seeded
* Side-effect free (no file IO, no global state)

### 9️⃣ Glossary
**Artifact**   
Minimal narrative generator producing structured outcomes.  
**Outcome**   
Symbolic narrative result (💀 / 🌿 / 🩸).  
**Manifest**   
Central registry describing artifact metadata and expected structure.  
**Determinism**  
Same inputs + same seed → same outcome.  


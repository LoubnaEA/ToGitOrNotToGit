# ✨ creatures_artifacts_reference

This document outlines all narrative artifacts in the Fate Engine.  
Each artifact defines one or more outcomes, a category, triggers and narrative notes.  

---

**Integration :** Source of truth for QA, runtime, API exposure.  
**Expansion potential :** Deterministic artifacts can later gain branching logic.  

**API Exposure Ex :**  
```python
from scripts.fate_engine import load_artifact
result = load_artifact("Hamlet")
````

**Testing Guide** to validate new artifacts :  
```bash
python scripts/playground/test_artifacts_loader.py --name Hamlet
```

This ensures :
* the artifact is correctly discovered
* its manifest entry is valid
* its outcomes structure matches the expected format  

For full runtime context, see **`scripts/playground/run_artifacts.py`** to execute all artifacts sequentially.

---

## 🧩 `scripts\artifacts`

### Duchess of Malfi
* **Outcomes :**
  * 💀 Secret revealed
  * 🌿 Secret survives
* **Category :** Court intrigue
* **Trigger :** Secrets and court pressures
* **Narrative note :** Political maneuvering can either protect or doom fragile secrets
* **Expansion potential :** Introduce randomized court events  
* **Code :** [duchess.py](../scripts/artifacts/duchess.py)  
* **Test :** `python scripts/playground/test_artifacts_loader.py --name Duchess`

### Euphues
* **Outcome :** 💀 Morality test failed
* **Category :** Moral allegory
* **Trigger :** Failed ethical reasoning
* **Narrative note :** Virtue alone cannot save Euphues; the system flags moral failure
* **Expansion potential :** Add more complex moral dilemmas.  
* **Code :** [euphues.py](../scripts/artifacts/euphues.py)  
* **Test :** `python scripts/playground/test_artifacts_loader.py --name Euphues`

### Faustus
* **Outcome :** 💀 Damnation inevitable
* **Category :** Morality / Pact
* **Trigger :** Pact level ≥ 3
* **Narrative note :** Forbidden knowledge locks Faustus into a determinist failure path
* **Expansion potential :** Could later include moral choices affecting outcomes.  
* **Code :** [faustus.py](../scripts/artifacts/faustus.py)  
* **Test :** `python scripts/playground/test_artifacts_loader.py --name Faustus`

### Hamlet
* **Outcome :** 💀 Ctrl+Z can't undo fate
* **Category :** Tragedy
* **Trigger :** Deterministic; narrative climax  
* **Narrative note :** Hamlet’s existential indecision seals his doom
* **Expansion potential :** Could later include multiple endings based on player choice
* **Code :** [hamlet.py](../scripts/artifacts/hamlet.py)  
* **Test :** `python scripts/playground/test_artifacts_loader.py --name Hamlet`

### Macbeth
* **Outcome :** 💀 Failed morality QA
* **Category :** Tragedy
* **Trigger :** Moral corruption threshold reached
* **Narrative note :** Ambition overwhelms Macbeth, ensuring failure regardless of intervention
* **Expansion potential :** Branching outcomes depending on interventions  
* **Code :** [macbeth.py](../scripts/artifacts/macbeth.py)  
* **Test :** `python scripts/playground/test_artifacts_loader.py --name Macbeth`

### Ophelia
* **Outcomes :**
  * grieving → 💀 Drowned
  * ignored → 💀 Lost mind
  * overwhelmed → 🌿 Survives
* **Category :** Psychological
* **Trigger :** Emotional stress levels
* **Narrative note :** Different stress contexts produce different fractures
* **Expansion potential :** Could introduce random events affecting survival  
* **Code :** [ophelia.py](../scripts/artifacts/ophelia.py)  
* **Test :** `python scripts/playground/test_artifacts_loader.py --name Ophelia`

### Random Fate
* **Outcomes :**
  * 🌿 Survives this act
  * 💀 Fatal outcome
* **Category :** Chaos
* **Trigger :** Randomized chance events
* **Narrative note :** Introduces unpredictability into the scenario pool 
* **Expansion potential :** Seeded randomness for deterministic QA testing  
* **Code :** [random_fate.py](../scripts/artifacts/random_fate.py)  
* **Test :** `python scripts/playground/test_artifacts_loader.py --name RandomFate`

### Spanish Tragedy
* **Outcome :** 💀 Escalation detected (max level 7)
* **Category :** Revenge drama
* **Trigger :** Sequence of revenge actions
* **Narrative note :** Revenge spirals out of control; deterministic escalation modeled
* **Expansion potential :** Could branch based on player decisions  
* **Code :** [spanish_tragedy.py](../scripts/artifacts/spanish_tragedy.py)  
* **Test :** `python scripts/playground/test_artifacts_loader.py --name SpanishTragedy`

---

### Testing & Validation
All narrative artifacts are covered by executable tests.

Validation includes :
- artifact discovery and loading  
  (the system automatically finds artifact definitions in the codebase and loads them at runtime)
- manifest consistency checks  
  (each artifact entry matches its declared metadata : name, category, outcomes, level, triggers)
- outcome structure validation  
  (all declared outcomes follow the expected schema and required fields)
- runtime execution without errors  
  (artifacts execute end-to-end without raising exceptions)

Relevant test entry points :
- `scripts/playground/test_artifacts_loader.py`
- `scripts/run_artifacts.py` (runtime smoke test)
- `tests/unit/`
- `tests/integration/`

### Why single-outcome artifacts still matter
Even deterministic artifacts are useful:
1. **Clarity & documentation**  
   No need to dive into code to understand the outcome.
2. **Consistency**  
   Same structure for all artifacts → easier automation.
3. **Future extensibility**  
   Can easily grow into multi-outcome artifacts without breaking anything.
4. **Testability**  
   QA and unit tests can lock expected outputs.
5. **API-ready**  
   Uniform structure simplifies dynamic loading and OpenAPI exposure.

### Summary
| Category            | #Artifacts | Typical Trigger          | Notes |
|---------------------|------------|--------------------------|-------|
| Tragedy             | 2          | Deterministic events     | Hamlet, Macbeth |
| Psychological       | 1          | Emotional stress         | Ophelia |
| Morality / Pact     | 1          | Pact level               | Faustus |
| Court intrigue      | 1          | Secrets & pressures      | Duchess of Malfi |
| Revenge drama       | 1          | Sequence actions         | Spanish Tragedy |
| Moral allegory      | 1          | Ethics test              | Euphues |
| Chaos               | 1          | Randomized events        | Random Fate |

### Symbols
- 💀 → Fatal / Failure  
- 🌿 → Survival / Success  
- 🩸 → Minor setback / Damage

### How to extend an artifact
Artifacts are designed to be **simple first, extensible later**.

To extend an existing artifact :
1. **Add new outcomes**  
   Expand the returned outcomes list to introduce branching results.
2. **Introduce conditional logic**  
   Use input parameters or thresholds (e.g. stress level, pact level, randomness).
3. **Preserve the contract**  
   The artifact must still expose a `generate()` function returning a list of outcomes.
4. **Update the manifest**  
   Reflect new categories, triggers or parameters in `artifacts_manifest.json`.
5. **Add or update tests**  
   Ensure deterministic paths and edge cases are covered by QA tests.

Artifacts can evolve from **deterministic** to **branching** without breaking :  
* the Fate Engine
* existing tests
* documentation or API consumers


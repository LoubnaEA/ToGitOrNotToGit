# ✨ creatures_scenarios

This document outlines all narrative `artifacts` in the Fate Engine.  
Each artifact has one or more outcomes, a category and contextual triggers.

---

**Integration :** This doc is the source of truth for QA, test creation and API exposure.  
**Expansion potential :** Deterministic artifacts can later gain branching logic.  
**API Exposure Example :**  
```python
from scripts.fate_engine import load_artifact
result = load_artifact("Hamlet")
````

**Testing Guide :**
To validate new artifacts :
```bash
python scripts/playground/test_artifacts_loader.py --name Hamlet
```

This ensures :
* the artifact is correctly discovered
* its manifest entry is valid
* its outcomes structure matches the expected format

---

## `scripts\artifacts`

### Hamlet
* **Outcome :** 💀 Ctrl+Z can't undo fate
* **Category :** Tragedy
* **Trigger :** Deterministic; always occurs at narrative climax
* **Narrative note :** Hamlet’s existential indecision seals his doom.
* **Expansion potential :** Could later include multiple endings based on player choice.


### Macbeth
* **Outcome :** 💀 Failed morality QA
* **Category :** Tragedy
* **Trigger :** Moral corruption threshold reached
* **Narrative note :** Ambition overwhelms Macbeth, ensuring failure regardless of intervention.


### Ophelia
* **Outcomes :**
  * grieving → 💀 Drowned
  * ignored → 💀 Lost mind
  * overwhelmed → 🌿 Survives
* **Category :** Psychological
* **Trigger :** Emotional stress levels
* **Narrative note :** Different stress contexts produce different fractures.


### Faustus
* **Outcome :** 💀 Damnation inevitable
* **Category :** Morality / Pact
* **Trigger :** Pact level ≥ 3
* **Narrative note :** Forbidden knowledge locks Faustus into a determinist failure path.


### Duchess of Malfi
* **Outcomes :**
  * 💀 Secret revealed
  * 🌿 Secret survives
* **Category :** Court intrigue
* **Trigger :** Secrets and court pressures
* **Narrative note :** Political maneuvering can either protect or doom fragile secrets.


### Spanish Tragedy
* **Outcome :** 💀 Escalation detected (max level 7)
* **Category :** Revenge drama
* **Trigger :** Sequence of revenge actions
* **Narrative note :** Revenge spirals out of control; deterministic escalation modeled.


### Euphues
* **Outcome :** 💀 Morality test failed
* **Category :** Moral allegory
* **Trigger :** Failed ethical reasoning
* **Narrative note :** Virtue alone cannot save Euphues; the system flags moral failure.


### Random Fate
* **Outcomes :**
  * 🌿 Survives this act
  * 💀 Fatal outcome
* **Category :** Chaos
* **Trigger :** Randomized chance events
* **Narrative note :** Introduces unpredictability into the scenario pool.


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


### Symbols
- 💀 → Fatal / Failure  
- 🌿 → Survival / Success  
- 🩸 → Minor setback / Damage  

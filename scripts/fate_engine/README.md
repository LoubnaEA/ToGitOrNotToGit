# 🔮 Fate Engine Runtime

The Fate Engine is a **narrative runtime** responsible for executing deterministic and semi-deterministic flows that transform textual inputs and contextual signals into structured narrative outputs.

It acts as the **central orchestration layer** between narrative artifacts, playground execution scripts and output generation.

The engine is intentionally lightweight and explicit, prioritizing **clarity, testability and extensibility** over complex modeling.

---

### 1️⃣ Architectural Role

The Fate Engine :
* Orchestrates the execution of narrative logic
* Provides **stable execution contracts** for artifacts and generators
* Ensures reproducible outcomes when deterministic or seeded
* Acts as a bridge between :
  * narrative artifacts
  * runtime playground scripts
  * future analytical or scoring layers

**Core Guarantees**
* Same input + same configuration → same output
* Clear separation between :
  * **artifacts** (narrative units)
  * **runtime orchestration**
  * **playground / experimentation**
* Stateless execution (no hidden side effects)

### 2️⃣ Directory Layout
```text
scripts/fate_engine/
├── prophecy_generator.py   → narrative outcome generator
├── text_parser.py          → text parsing utilities
├── visual_helper.py        → output / display helpers
└── __init__.py
```

The Fate Engine does not execute autonomously.
It is always invoked by runtime scripts located in `scripts/playground/`

### 3️⃣ Execution Model

**Narrative Flow**
```text
Input Text / Context
↓
Optional Parsing (text_parser)
↓
Narrative Generation (prophecy_generator or artifacts)
↓
Formatting / Display Helpers
↓
Structured Output
```

Each execution step is intentionally explicit and inspectable, making the pipeline easy to test and reason about.

### 4️⃣ Output Structure

A Fate Engine execution typically produces :
* A narrative outcome (string or structured text)
* Optional metadata (scenario, seed, execution mode)
* Optional persisted outputs (text files, visuals)

Ex conceptual output :
```json
{
  "outcome": "💀 Ambition seals the fate",
  "meta": {
    "scenario": "macbeth",
    "execution_mode": "deterministic"
  }
}
```
The output structure is designed to remain **JSON-safe** and compatible with future analytical or visualization layers.

### 5️⃣ Usage Example
```python
from scripts.fate_engine.prophecy_generator import generate_prophecy

result = generate_prophecy(character="Hamlet")
print(result)
```

Or via runtime scripts :
```bash
python scripts/playground/run_fate_engine.py
```

### 6️⃣ Error & Stability Model

The Fate Engine follows a **fail-fast philosophy** :
* Invalid inputs raise explicit Python errors
* Missing artifacts or unsupported scenarios are reported clearly
* Runtime scripts act as smoke tests for engine stability

### 7️⃣ Testing & Validation

The Fate Engine is covered by :
* Unit tests for core generators and utilities
* Integration tests through playground scripts
* Smoke tests via full artifact execution

See `tests/README.md` for the full testing strategy.

### 8️⃣ Future Expansion (Planned & Possible)

The current Fate Engine intentionally avoids heavy analytics.
However, its structure allows future extensions such as :
* Narrative weighting or scoring layers
* Branching logic based on contextual thresholds
* Normalization or aggregation of multiple outcomes
* Integration with data-driven or ML-based evaluators
* API exposure for external narrative consumers

These enhancements can be added **without breaking existing artifacts or runtime scripts**.

### 9️⃣ Design Philosophy
* Explicit > implicit
* Testable > clever
* Narrative clarity > opaque abstraction

The Fate Engine is not a black box.  
It is a readable, extensible runtime designed to evolve alongside the project.   


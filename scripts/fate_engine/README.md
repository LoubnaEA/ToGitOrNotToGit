# Fate Engine Runtime

The Fate Engine executes the full analytical pipeline used to convert raw text into structured insights.  
It defines the scoring graph, reduction layers, normalization rules, output schema consumed by upper modules.

---

### 1. Architectural Role
- Acts as the **runtime orchestrator** for all fate-scoring operations.  
- Provides **stable contracts** for pipeline nodes (scorers, reducers, normalizers).  
- Ensures deterministic, reproducible results across datasets.
#### Core Guarantees
- Same input → same output (deterministic mode)
- All steps follow the **Fate IO Schema**
- Pipeline execution isolated from EDA and artifacts layers


### 2. Directory Layout
scripts/fate_engine/  
├── engine.py        → master orchestrator, run_fate(), pipeline execution  
├── scorers.py       → scoring functions, semantic weight maps  
├── reducers.py      → text normalization, compression, cleanup rules  
└── utils.py         → shared helpers (token ops, guards, transformations)  


### 3. Execution Model
#### Pipeline Contract
Each stage receives a **FateInput** and returns a **FateOutput** :
```
Raw Text
↓
Tokenization (optional pre-step)
↓
Scorers            → assigns semantic weights
↓
Reducers           → compress, normalize, filter noise
↓
Final Composer     → structured output map
````

#### Fate Output Schema
A valid Fate output always contains :
```json
{
  "weights": { ... },         // semantic or structural weights
  "layers": { ... },          // reduced/compressed layers
  "meta": {                   // runtime metadata
      "version": "x.y.z",
      "execution_mode": "deterministic"
  }
}
````


### 4. Usage Example 
```python
from fate_engine.engine import run_fate
result = run_fate("All the world's a stage, and all the men and women merely players.")
print(result["weights"])
```


### 5. Error Model
| Code    | Error Type            | Trigger                           |
| ------- | --------------------- | --------------------------------- |
| FATE-01 | InvalidPipelineState  | Missing or misconfigured stage    |
| FATE-02 | ScoringError          | Weight calculation failure        |
| FATE-03 | ReductionError        | Normalization/compression failure |
| FATE-04 | FateOutputSchemaError | Output missing required fields    |


### 6. Test Execution
```bash
pytest -q scripts/fate_engine
```
Tests cover :
* Node-level behavior
* Pipeline determinism
* Fate Output Schema validation


### 7. Promotion Rules (Dev → Stable)
A new pipeline stage becomes **stable** when :
1. It defines a clear input/output contract
2. It is deterministic
3. It is used by `run_fate()` without optional flags
4. All Fate Output Schema tests pass


### 8. Compatibility Notes
* Python ≥ 3.10
* Engine designed to be stateless and side-effect-free
* Compatible with JSON-safe outputs for downstream analysis


### 9. Glossary
**Scorer** : Computes semantic or structural weights.
**Reducer** : Normalizes or compresses intermediate results.
**Pipeline Node** : Atomic step in the Fate runtime.
**Fate Output** : Final structured result consumed by other modules.


---



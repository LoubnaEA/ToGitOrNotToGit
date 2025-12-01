# Artifacts Registry Layer

Centralized layer responsible for the creation, validation, storage and retrieval of all persistent artifacts produced within the analysis pipeline.    
Provides reliability guarantees, version safety, consistent IO semantics across modules.

--- 

### 1️⃣ Scope & Responsibilities
#### Core Contracts
- **Stable serialization** for dictionaries, lists, statistical maps, model-like objects.  
- **Deterministic loading** with type validation and optional schema checks.  
- **Version-safe naming** : components can evolve without breaking downstream consumers.
- **Isolation** : artifacts stored here never contain business logic.
#### Not Included
- No domain computation  
- No visualization generation  
- No fate scoring logic  


### 2️⃣ Directory Layout
scripts/artifacts/  
├── save_artifact.py      → write interfaces (json, pickle-safe, text)  
├── load_artifact.py      → read interfaces with optional validation  
├── artifact_utils.py     → hashing, versioning, path helpers  
└── samples/              → minimal example artifacts (dev/debug)  


### 3️⃣ IO Specifications
#### Write API, Guarantees
- Writes are **atomic** (tempfile → final).
- Output is **human-inspectable** when possible (JSON-first).
- Every write operation returns a **ResolvedArtifactPath**.
### Read API, Guarantees
- Fails with **explicit error classes** (no silent fallbacks).
- Guarantees **shape fidelity** (same type as original input).
- Optional checksum verification (via `artifact_utils`).


### 4️⃣ Usage Examples
#### Save JSON
```python
from artifacts.save_artifact import save_json
save_json({"counts": tokens}, "token_map.json")
````
#### Load JSON
```python
from artifacts.load_artifact import load_json
tokens = load_json("token_map.json")
```
#### Save Python Object (safe-pickle)
```python
from artifacts.save_artifact import save_pickle
save_pickle(model, "ngram_model.pkl")
```


### 5️⃣ Error Model
| Code   | Error Type          | Trigger                                 |
| ------ | ------------------- | --------------------------------------- |
| ART-01 | InvalidArtifactPath | File missing / invalid extension        |
| ART-02 | ArtifactReadError   | Corrupted file / failed deserialization |
| ART-03 | ArtifactSchemaError | Shape mismatch when validation enabled  |
| ART-04 | ArtifactWriteError  | Insufficient permissions or disk issues |


### 6️⃣ Test Execution
Artifacts follow strict IO policies and are fully covered with unit tests.
```bash
pytest -q scripts/artifacts
```


### 7️⃣ Promotion Rules (Dev → Stable)
A new artifact format becomes *stable* when :
1. It is produced by a stable module
2. A matching loader exists
3. Round-trip tests (save → load) succeed


### 8️⃣ Compatibility Notes
* Python ≥ 3.10
* JSON outputs are UTF-8 normalized
* Pickle mode restricted to safe protocol levels (no arbitrary code execution)


### 9️⃣ Glossary
**Artifact** : Any persisted output required by other modules.  
**IO Contract** : Rules ensuring loading always matches the saved type/shape.  
**Round-trip Safety** : Guarantee that `load(save(x)) == x`.  


```
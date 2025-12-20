# Test Strategy for Narrative Pipeline

The Fate Engine and its narrative artifacts are fully covered by a structured testing approach.  
All artifacts and scripts have been tested to ensure correctness, discoverability, and runtime stability.

This ensures that every component of the narrative pipeline is reliable, testable, properly documented.

---

## 🧩 Testing & Validation

### 1️⃣ Test Goals

- **Artifact discovery and loading**  
  Ensure all artifacts are properly detected by the engine and available via `load_artifact()`  
- **Manifest consistency checks**  
  Validate that each artifact has a corresponding entry in `artifacts_manifest.json`  
- **Outcome structure validation**  
  Confirm that `generate()` functions return outputs in the expected format.  
- **Runtime execution without errors**  
  All runtime scripts (`run_artifacts.py`, `run_fate_engine.py`, etc.) execute successfully.

### 2️⃣ Test Framework

- **Unit tests :** Located in `tests/unit/`, e.g., `test_prophecy_generator.py`
- **Integration tests :** Located in `tests/integration/`, e.g., `test_fate_engine_flow.py`   
- **Smoke tests**: Running `scripts/playground/run_artifacts.py` ensures all artifacts can be executed sequentially without errors.  
- **Contract testing :** Checks alignment between artifact outputs and manifest specifications.

### 3️⃣ How to Run Tests

**Unit / Integration**
```bash
pytest tests/unit
pytest tests/integration
````
**Test a specific artifact**
```bash
python scripts/playground/test_artifacts_loader.py --name Hamlet
python scripts/playground/test_artifacts_loader.py --name RandomFate
```
**Run all artifacts (smoke test)**
```bash
python -m scripts.run_artifacts
```

### 4️⃣ Test Coverage Notes

✅ All 8 narrative artifacts tested individually.  
✅ Prophecy generator and Fate Engine core scripts tested for output consistency.  
✅ Runtime scripts (`run_fate_engine.py`, `runner_prophecy.py`) tested in playground scenarios.  
✅ Outputs verified to be deterministic or reproducible when seeded.  

### 5️⃣ Extending Tests
- To test new artifacts :
  - **Add** the artifact to `scripts/artifacts/`.
  - **Update** `artifacts_manifest.json`.
  - **Run** :
  ```bash
  python scripts/playground/test_artifacts_loader.py --name NewArtifact
  ```
New runtime scripts can be validated via smoke tests with `run_artifacts.py`

### 6️⃣ Symbols & Conventions
* 💀 → Fatal / Failure outcome
* 🌿 → Survival / Success outcome
* 🩸 → Minor setback / Damage


# scripts/fate_engine/__init__.py

from pathlib import Path
import json


# Path to the JSON file
BASE_DIR = Path(__file__).parent.parent           # References the scripts/ directory
MANIFEST_FILE = BASE_DIR / "artifacts" / "artifacts_manifest.json"

# Function to retrieve the names
def get_artifact_names():
    """
    Returns the list of artifact names from artifacts_manifest.json
    In this JSON, the artifact names are the main dictionary keys
    """
    if not MANIFEST_FILE.exists():
        raise FileNotFoundError(f"Manifest file not found : {MANIFEST_FILE}")
    
    with MANIFEST_FILE.open("r", encoding="utf-8") as f:
        data = json.load(f)

    return list(data.keys())     # The names of the artifacts = the keys of the dictionary

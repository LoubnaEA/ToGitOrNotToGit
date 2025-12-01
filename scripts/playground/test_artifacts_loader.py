from scripts.fate_engine import get_artifact_names, load_artifact

def test_all_artifacts():
    print("🔹 Listing all artifacts :")
    artifact_names = get_artifact_names()
    print(artifact_names)
    print("\n🔹 Testing artifact generation :")

    for name in artifact_names:
        try:
            generate_fn = load_artifact(name)
            result = generate_fn()
            print(f"{name}: {result}")
        except Exception as e:
            print(f"{name}: ❌ Failed to load or generate - {e}")

if __name__ == "__main__":
    test_all_artifacts()

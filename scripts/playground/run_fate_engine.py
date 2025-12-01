"""Manual runner to generate and save artifacts from the fate engine"""

from datetime import datetime
from scripts.fate_engine.prophecy_generator import generate_prophecy

def run_example(character_name="Unknown Soul"):
    # Generate prophecy
    prophecy = generate_prophecy(character_name)

    # Display in console
    print("\n=== PROPHECY GENERATED ===\n")
    print(prophecy)
    print("\n==========================\n")

    # Save to artifacts/
    filename = f"artifact_{character_name.lower()}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    filepath = f"scripts/artifacts/{filename}"

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(prophecy)

    print(f"Artifact saved → {filepath}")

if __name__ == "__main__":
    run_example("Ophelia")

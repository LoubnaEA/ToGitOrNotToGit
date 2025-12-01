import random
import sys
import os

# -----------------------------
# Prophecies pool
# -----------------------------
PROPHECIES = [
    "You will find great fortune",
    "Beware of the ides of March",
    "A thrilling adventure awaits you",
    "Someone close to you will surprise you",
    "Change is coming ; embrace it",
    "Your ambition may be your undoing",
    "A secret betrayal is near",
    "Love will test your resolve",
    "The fates are watching closely",
    "A sudden twist will shape your destiny"
]
# Core generator function
# -----------------------------
def generate_prophecy(character=None):
    """
    Generates a random prophecy.
    Includes a specified character name in the text, if provided.
    """
    prophecy = random.choice(PROPHECIES)
    if character:
        prophecy = f"{character}: {prophecy}"
    return prophecy

# Wrapper class
# -----------------------------
class ProphecyGenerator:
    """Wrapper around generate_prophecy with default character"""
    
    def __init__(self, default_character=None):
        self.default_character = default_character

    def generate(self, character=None):
        return generate_prophecy(character or self.default_character)

# Script mode : generate prophecy for scenario
# -----------------------------
if __name__ == "__main__":
    # Default scenarios
    SUPPORTED_SCENARIOS = ["hamlet", "macbeth", "romeo", "juliet"]

    # Parse scenario argument
    scenario = None
    if len(sys.argv) > 1:
        for i, arg in enumerate(sys.argv):
            if arg in ["--scenario", "-s"] and i + 1 < len(sys.argv):
                scenario = sys.argv[i + 1].lower()

    # Validate scenario
    if scenario not in SUPPORTED_SCENARIOS:
        print(f"⚠️ Scenario not supported or missing. Using default: 'hamlet'")
        scenario = "hamlet"

    # Generate prophecy
    generator = ProphecyGenerator(default_character=scenario.capitalize())
    output = generator.generate()

    # Ensure output folder exists
    output_dir = os.path.join("visuals", "fate_outputs")
    os.makedirs(output_dir, exist_ok=True)

    # Save output to file
    output_file = os.path.join(output_dir, f"{scenario}_output.txt")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(output + "\n")

    # Print confirmation
    print(f"✅ Prophecy for '{scenario}' saved to {output_file}")
    print(output)

# shakespearean_fate.py 
# Generates a Shakespeare-style fate or prophecy related to code quality and developer actions

import random

FATES = [
    "Thy commit, though bold, hath broken tests unknown to mortal eyes.",
    "A merge conflict awaits thee, woven by unseen branches.",
    "Push not tonight, for the linter’s wrath shall smite thee.",
    "Refactor thou must, or bugs shall bloom like poisoned roses.",
    "Beware the feature flag, for it hideth serpents beneath its cloak.",
]

def divine_fate(seed: int | None = None) -> str:
    if seed is not None:                 # Optional 'seed' makes randomness reproducible for testing or debugging
        random.seed(seed)                   # If provided, it forces Python's random generator to behave deterministically
    return random.choice(FATES)                # Select and return one prophecy at random from the list above

# This block runs only when this file is executed directly
# It does NOT run if the file is imported as a module in another script
if __name__ == "__main__":
    print(divine_fate())

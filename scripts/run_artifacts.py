# scripts/run_artifacts.py

"""
Simple runner that calls each artifact and prints one-line outputs
Run with : python -m scripts.artifacts.run_artifacts
"""

from .artifacts.hamlet import to_be_or_not_to_be
from .artifacts.macbeth import regicide
from .artifacts.ophelia import succumb_to_despair
from .artifacts.faustus import bargain
from .artifacts.duchess import tragic_secret
from .artifacts.spanish_tragedy import revenge_cycle_summary
from .artifacts.euphues import moral_temptation
from .artifacts.random_fate import destiny_once

def print_separator():
    print("\n" + "-" * 50 + "\n")

def run_all():
    print_separator()
    print("Hamlet Artifact :")
    print(to_be_or_not_to_be("not to be"))

    print_separator()
    print("Macbeth Artifact :")
    print(regicide("Macbeth"))

    print_separator()
    print("Ophelia Artifact :")
    print(succumb_to_despair("grieving"))

    print_separator()
    print("Faustus Artifact :")
    print(bargain(3))

    print_separator()
    print("Duchess of Malfi Artifact :")
    print(tragic_secret(seed=42))  # deterministic example for run

    print_separator()
    print("Spanish Tragedy Artifact :")
    print(revenge_cycle_summary([2, 6, 4, 7]))

    print_separator()
    print("Euphues Artifact :")
    print(moral_temptation("corrupt"))

    print_separator()
    print("Random Fate Artifact :")
    print(destiny_once(seed=12345))  # deterministic example

    print_separator()
    print("🔥 All artifacts executed successfully 🔥")

if __name__ == "__main__":
    run_all()

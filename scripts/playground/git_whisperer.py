# git_whisperer.py
# Reads the silent murmurs of your Git repository and returns a dark prophecy

import subprocess
import random

def _run(cmd: list[str]) -> str:         # Helper function to safely run a command and return its output
    try:
        return subprocess.check_output(cmd, stderr=subprocess.STDOUT).decode("utf-8").strip()
    except Exception:
        return ""                        # Return empty string if the command fails

def git_whisper() -> str:                # Get uncommitted changes (status) and current branch name
    status = _run(["git", "status", "--porcelain"])
    branch = _run(["git", "rev-parse", "--abbrev-ref", "HEAD"])

    if not branch:
        return "The repository is silent, no Git spirits reside here."    # If not in a Git repository

    if status:                                                             # If there are uncommitted changes, warn the user
        omen = f"Your branch '{branch}' bleeds with uncommitted changes. The shadows urge : commit, or face chaos."
    else:
        # If everything is clean.
        omen = f"Branch '{branch}' rests in eerie stillness… yet whispers of a forgotten stash."

    extras = [                                        # Extra random warning to add flavor
        "Merge conflicts brew like storm clouds.",
        "A rebase awaits, thirsting for discipline.",
        "Your commit history hides a secret regret.",
        "A detached HEAD wanders nearby… do not follow it.",
    ]

    return f"{omen} {random.choice(extras)}"

if __name__ == "__main__":        # Only execute this block when running the script directly
    print(git_whisper())

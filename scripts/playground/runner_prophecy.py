# runner_prophecy.py
# Summons all omens and weaves them into a final prophecy scroll

from shakespearean_fate import divine_fate
from python_omens import detect_omen
from git_whisperer import git_whisper

SEPARATOR = "\n" + ("-" * 72) + "\n"       # Visual separator for the report

def run_all_prophecies() -> str:           # Call each prophecy-generating module
    fate = divine_fate()
    omen = detect_omen()
    git_msg = git_whisper()

    report = (                             # Assemble the report with titles and separators
        "🕯️  THE PROPHETIC SCROLL OF CODE & COMMITS  🕯️\n"
        + SEPARATOR +
        "⏳ Shakespearean Fate:\n" +
        fate +
        SEPARATOR +
        "🐍 Pythonic Omen:\n" +
        omen +
        SEPARATOR +
        "🌑 Git Whisper:\n" +
        git_msg +
        SEPARATOR +
        "End of scroll."
    )

    return report
if __name__ == "__main__":                 # Only execute this block when running the script directly
    print(run_all_prophecies())

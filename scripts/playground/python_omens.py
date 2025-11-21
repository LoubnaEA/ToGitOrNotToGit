# python_omens.py 
# Interprets mystical omens from the Python runtime environment

import sys
import platform
import random

def detect_omen() -> str:
    # Get Python version (major and minor numbers)
    version = sys.version_info
    major_minor = f"{version.major}.{version.minor}"

    os_name = platform.system()         # Detect operating system to enable platform-specific logic

    omens = [
        f"The Python spirits whisper : version {major_minor} is fickle on {os_name}. Beware incompatible wheels.",
        f"In the shadows of {os_name}, your interpreter mutters warnings of deprecated modules.",
        f"Version {major_minor} awakens ancient bugs if thou importeth 'random' excessively.",
        "The memory usage swells like a tide—allocate wisely, lest the OOM demon feast upon your notebook.",
        "A cursed dependency lies dormant in thy environment.txt—update or be doomed."
    ]
    return random.choice(omens)

if __name__ == "__main__":               # Only execute this block when running the script directly
    print(detect_omen())

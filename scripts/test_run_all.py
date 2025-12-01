# scripts/test_run_all.py

import subprocess
import sys
import os
import pandas as pd


# CSV/MD file validation
# =========================================
print("🔹 Validating datasets…")
datasets = [
    "data/raw/creatures_raw_dataset.csv",
    "data/raw/dark_stage_raw_dataset.md",
]

for path in datasets:
    if os.path.exists(path):
        print(f"✅ {path} found")
    else:
        print(f"❌ {path} missing !")

# Optional : quick read test
try:
    pd.read_csv("data/raw/creatures_raw_dataset.csv", sep="\\")
    print("✅ creatures_raw_dataset.csv loaded correctly")
except Exception as e:
    print(f"❌ Error reading creatures_raw_dataset.csv : {e}")


# Run EDA scripts
# =========================================
eda_scripts = [
    "scripts/eda/eda_creatures_01_stats.py",
    "scripts/eda/eda_creatures_02_cleaning.py",
    "scripts/eda/eda_creatures_03_visuals.py",
    "scripts/eda/eda_creatures_04_quality_checks.py",
    "scripts/eda/eda_dark_stage.py"
]

print("\n🔹 Running EDA scripts…")
for script in eda_scripts:
    print(f"\n--- {script} ---")
    result = subprocess.run([sys.executable, script], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"✅ {script} executed without errors")
    else:
        print(f"❌ {script} encountered an error")
        print(result.stderr)


#  Run the artifact engine
# =========================================
print("\n🔹 Test run_artifacts.py…")
try:
    subprocess.run([sys.executable, "-m", "scripts.run_artifacts"], check=True)
    print("✅ run_artifacts.py executed victoriously")
except subprocess.CalledProcessError as e:
    print(f"❌ run_artifacts.py encountered an error: {e}")




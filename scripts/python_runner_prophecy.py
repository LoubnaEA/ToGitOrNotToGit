import sys

def run_prophecy():
print("The prophecy has run")
return 0

if __name__ == "__main__":
try:
exit_code = run_prophecy()
sys.exit(exit_code)
except Exception as e:
print(f"The prophecy has failed: {e}")
sys.exit(1)
import subprocess
import sys

# Pre-defined inputs
inputs = [
    "261",      # 24600 CE current price
    "130",      # 25000 CE current price
    "232",      # 23700 PE current price
    "144"       # 23300 PE current price
]

# Run nt.py with these inputs
input_str = "\n".join(inputs) + "\n"
process = subprocess.Popen(
    [sys.executable, "nt.py"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

stdout, stderr = process.communicate(input=input_str)
print(stdout)
if stderr:
    print(f"Error: {stderr}", file=sys.stderr)

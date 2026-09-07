import glob
import subprocess
import sys

notebooks = sorted(
    f for f in glob.glob("*.ipynb")
    if not f.startswith("executed_")
)

for notebook in notebooks:
    print(f"\n===== Executing {notebook} =====")
    subprocess.run(
        [sys.executable, "-m", "jupyter", "nbconvert",
         "--to", "notebook", "--execute", "--inplace", notebook],
        check=True
    )

print("\nAll 10 notebooks executed successfully.")

import os, subprocess, sys

notebooks = sorted(f for f in os.listdir(".") if f.endswith(".ipynb") and f != "run_all_notebooks.ipynb")
for nb in notebooks:
    print(f"\n===== Running {nb} =====")
    subprocess.run([sys.executable, "-m", "jupyter", "nbconvert", "--to", "notebook",
                    "--execute", "--inplace", nb], check=True)
print("\nAll worksheets executed successfully.")

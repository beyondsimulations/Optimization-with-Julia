from pathlib import Path

import jupytext

# Derive a .jl percent file from every rendered notebook. The notebook stays in
# _site: this workshop offers both downloads (Applied-Optimization deletes it).
for notebook_path in Path("_site").rglob("*.ipynb"):
    # Read the notebook
    notebook = jupytext.read(notebook_path)

    # Define output path (same name, .jl extension)
    output_path = notebook_path.with_suffix(".jl")

    # Write as percent format
    jupytext.write(notebook, output_path, fmt="py:percent")

    print(f"Converted: {notebook_path} -> {output_path}")

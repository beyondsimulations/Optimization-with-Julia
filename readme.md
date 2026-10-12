# Optimization with Julia

A comprehensive course on mathematical optimization using Julia, JuMP, and HiGHS. This course is designed to take you from basic Julia programming to solving complex optimization problems.

## Course Overview

This course is structured in three main parts:

1. **First Steps**: Basic Julia programming concepts
   - Variables and Types
   - Vectors and Matrices
   - Comparisons
   - Loops
   - Dictionaries

2. **Data Handling**: Working with data in Julia
   - Functions
   - Package Management
   - DataFrames
   - Input/Output Operations
   - Plotting

3. **Optimization**: Mathematical optimization with JuMP
   - Introduction to JuMP
   - Variables and Bounds
   - Constraints
   - Advanced Solver Options
   - Transportation Problems

## Prerequisites

- Basic programming knowledge recommended
- Julia (latest version recommended)
- Zed with the Julia extension (fallback: VS Code with the Julia extension)

## Getting Started

1. Install Julia from [julialang.org](https://julialang.org)
2. Install Zed from [zed.dev](https://zed.dev)
3. Install the Julia extension in Zed (command palette, **zed: extensions**)
4. Follow the "Julia in Zed" steps of the [first tutorial](https://beyondsimulations.github.io/Optimization-with-Julia/part-01/tutorial-01-01-variables.html): they set up the workshop environment and the kernel Zed runs the code with
5. Download the tutorials from the [website](https://beyondsimulations.github.io/Optimization-with-Julia) as `.jl` files (or as `.ipynb` notebooks) and start with the introduction section

## Building the Site

The site is built with [Quarto](https://quarto.org) and its native Julia engine (Julia 1.13); Python is only needed for the helper scripts and is managed with [uv](https://docs.astral.sh/uv/).

```bash
julia --project=. -e 'using Pkg; Pkg.instantiate()'  # Julia packages
uv sync                                               # Python packages
uv run quarto render                                  # website in _site/
```

After the render, `helpers/convert_pypercent.py` derives a `.jl` file in percent format (`# %%` cells) from every tutorial notebook. Both stay on the site: each tutorial page links the `.jl` file ("Julia") and the notebook ("Jupyter").

## Course Structure

Each tutorial includes:
- Theoretical explanations
- Code examples
- Interactive exercises
- Solutions (in the solutions folder)

## License

CC BY-SA 4.0 - See LICENSE file for details

## Additional Resources

- [Julia Documentation](https://docs.julialang.org/)
- [JuMP Documentation](https://jump.dev/JuMP.jl/stable/)
- Recommended books:
  - "Think Julia: How to think like a computer scientist" by Lauwens & Downey
  - "Julia programming for operations research" by Kwon

## Contributing

Feel free to:
- Report issues
- Suggest improvements
- Submit pull requests

## Contact

- GitHub: [beyondsimulations/Optimization-with-Julia](https://github.com/beyondsimulations/Optimization-with-Julia)
- LinkedIn: [Tobias Vlćek](https://linkedin.com/in/tobiasvlcek)

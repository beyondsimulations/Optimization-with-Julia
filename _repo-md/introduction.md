# Introduction
Dr. Tobias Vlćek

# <span class="flow">Julia Programming Language</span>

## Why Julia?

- **Designed to be:**
  - as general as Python
  - as statistics-friendly as R
  - as fast as C++!

> [!TIP]
>
> **Allows for fast data workflows**, particularly in scientific
> computing!

## Syntax

- Dynamically-typed syntax just like Python
- Similar to R, Matlab and Python - **not like C++**
- In comparison, accessible and easy to learn!
- **No need to worry about memory management!**

## JuMP

- Package for **algebraic modeling** in Julia
- Simplifies solving complex optimization problems
- Provides a high-level, user-friendly interface
- Useful for operations research and data science

> [!TIP]
>
> JuMP is an alternative to Pyomo, GAMS, and AMPL!

# <span class="flow">Algebraic Modeling</span>

## What is algebraic modeling?

- A “mathematical language” for optimization problems
- Allows for describing complex systems and constraints
- Based on linear algebra (Equations and Inequalities)

## How to learn algebraic modeling?

- **Practice, practice, and practice!**
- Understand standard models and their approach
- Develop an understanding of constraints
- Understand the structure of a models solution space
- Use an available algorithms to determine solutions

## Central Questions

- What is to be decided?
- What is relevant to the decision?
- What information is given and relevant?
- What parameters (data) are needed?
- Which variables and of which type are needed?

> [!TIP]
>
> Modeling is a creative process!

## Model Components

1.  Objective function
2.  Constraints
3.  Variables

## Linear Optimization Model

#### Basic Model Formulation

$$
\begin{aligned}
&\text{maximize} \quad F = \sum_{j\in \mathcal{J}} c_j \times X_j
\end{aligned}
$$

subject to

$$
\begin{aligned}
&\sum_{j\in \mathcal{J}} a_{i,j} \times X_j  \le b_i && \forall i \in \mathcal{I} \\
&X_j \ge 0 &&  \forall  j \in \mathcal{J} 
\end{aligned}
$$

#### Model Components

$$
\begin{aligned}
\mathcal{I} &: \text{set of $i \in \mathcal{I}$,}\\
\mathcal{J} &: \text{set of $j \in \mathcal{J}$,}\\
F   &: \text{Objective function variable,}\\
X_{j}   &: \text{decision variables,}\\
c_{j}   &: \text{objective function coefficients,}\\
a_{i,j} &: \text{parameters,}\\
b_{i}   &: \text{parameters}
\end{aligned}
$$

## What is modelling good for?

- <span class="highlight">Good Question!</span> A lot of things:
  - Modeling real-world problems
  - Solving complex systems
  - Optimizing resource allocation
  - Decision-making under constraints
  - Simulation and prediction

# <span class="flow">Installing Julia</span>

## Download and Install Julia

To prepare for the upcoming lectures, we start by installing the Julia
Programming Language and an Integrated Development Environment (IDE) to
work with Julia.

## Installing Julia

<img src="https://images.beyondsimulations.com/ao/ao_julia2.png"
data-max-width="400px" />

- Head to [julialang.org](https://julialang.org) and follow the
  instructions.

> [!TIP]
>
> If you are ever asked to add something to your “PATH”, do so!

## VS Code

- Next, we are going to install VS Code
- Alternatively, you can install VS Codium
- It is essentially VS Code but without any tracking by MS

## Installing VS Code

- Head to the website
  [code.visualstudio.com](https://code.visualstudio.com)
- OR to the webside [vscodium.com](https://vscodium.com)
- Download and install the latest release

## Verify the Installation

- Start the IDE and take a look around
- Search for the field “Extensions” on the left sidebar
- Click it and search for “Julia”
- Download and install “Julia (Julia Language Support)”

## Create a new file

- Create a new file with a “.jl” ending
- Save it somewhere on your computer
- e.g., in a folder that you will use in the course

``` julia
print("Hello World!")
```

    Hello World!

- Run the file by clicking “run” in the upper right corner
- OR by pressing “Control+Enter” or “STRG+Enter”

## Everything working?

- If the terminal opens with a `Hello World!` → perfect!
- If not, it is likely that the IDE <span class="highlight">cannot find
  the path</span> to Julia
- Try to determine the path and save it to VS Code
- After saving it, try to run the file again

## How to get started?

- Following three parts are dedicated to learning the basics
- Start with the very basics and gradually move on
- Focus in the first two parts on the programming language
- Third part dedicated to <span class="highlight">Mathematical
  Optimization</span>

# <span class="flow">Working with VS Code</span>

## Notebooks in VS Code

- The easiest way is by using VS Code
- Install the Jupyter Extension
- Now, you can open `.ipynb` files
- Here you can run the code in the cells

## Downloading the Notebooks

- You will find the notebooks next to the sections pages
- On each page, you will find a button `Jupyter` on the right
- Click it to download the notebook and save it
- I’d recommend storing the notebooks <span class="highlight">in a
  separate directory for this workshop</span>

# <span class="flow">Working with IJulia</span>

## IJulia

- IJulia is an interface between Julia and Jupyter Notebooks
- Popular tool for data analysis and visualization
- You can use IJulia to run <span class="highlight">Julia code in the
  notebooks</span>

## Installing IJulia

- Open the VS Code IDE and start a terminal
- Start Julia by typing `julia` in the terminal
- Install IJulia by typing `]` to open the package manager
- Install IJulia by typing `add IJulia`
- Press `Enter`

## Running IJulia

``` julia
using IJulia; notebook()
```

- Start IJulia by typing the above code in the Julia prompt
- This will open a new browser window
- You can now run code in the notebooks

> [!NOTE]
>
> You can also run the notebooks in VS Code, if you prefer!

## Get started with the sections

- Download the first notebook and open it
- Start with the <span class="highlight">first problem and solve it step
  by step</span>
- You can find the sections here on the website
- <span class="highlight">You can ask questions anytime!</span>

# <span class="flow">Literature</span>

## Literature

For interesting literature to learn more about Julia, take a look at the
[literature list](general/literature.qmd) of this course.

"""Build the workshop solutions from the rendered tutorial notebooks.

usage: uv run python helpers/sync/build_solutions.py <_site dir> <out dir>

For every tutorial, the notebook students download is read from _site, each
exercise cell (marked YOUR CODE BELOW / YOUR CHANGES BELOW) gets its solution,
and the result is written as .jl (percent) and .ipynb, so both are the same
notebook. A str is appended to the cell, a tuple ("replace", text) replaces it.
Stops if the number of exercise cells and solutions differ: a new exercise
needs its solution in SOLUTIONS, in the order of the tutorial.
"""
import sys
from pathlib import Path

import jupytext

SITE, OUT = Path(sys.argv[1]), Path(sys.argv[2])

SOLUTIONS = {
    "part-01/tutorial-01-01-variables": [
        "x = 1",
        'hi = "Hello, Optimization!"',
        "answerUniverse = 42",
        "money = 1.35",
        "isStudent = true",
        "y::Int64 = 5",
        'message = "y is $y"',
    ],
    "part-01/tutorial-01-02-vectors": [
        "fib = [1, 1, 2, 3, 5]",
        "push!(fib, 8)",
        "popfirst!(fib)",
        "first_three_elements = fib[1:3]",
        "my_matrix = [1 2 3; 4 5 6]",
        "my_matrix[2, 3] = 17",
        "added_matrices = my_matrix + another_matrix",
        "added_matrices .+= 10",
        'my_tuple = (4.0, added_matrices, "Hi there!")',
        "second_element = my_tuple[2]",
    ],
    "part-01/tutorial-01-03-comparisons": [
        "comparison1 = (10 > 5)",
        'x = "Hello"\ny = "world"\ncomparison2 = (x != y)',
        'logic1 = (10 > 5) && ("hello" == "hello")',
        'logic2 = (10 < 5) || ("hello" == "hello")',
        "logic3 = (10 > 5)\nlogic4 = !logic3",
        "chained_comparison = (1 < x < 10)",
    ],
    # `global` is only needed when the file runs as a script, see the tutorial
    "part-01/tutorial-01-04-loops": [
        "for i in 1:5\n    global sum_numbers += i\nend",
        "for i in 1:10\n    if i % 2 == 0\n        global sum_evens += i\n    end\nend",
        'for fruit in fruits\n    global current_fruit = fruit\n    if current_fruit == "banana"\n        break\n    end\nend',
        "while current_value >= 3\n    global current_value -= 1\nend",
        "while true\n    global first_multiple_of_7 += 7\n    if first_multiple_of_7 > 50\n        break\n    end\nend",
        "for number1 in numbers1\n    for number2 in numbers2\n        push!(products, number1 * number2)\n    end\nend",
        "even_numbers = [i for i in 1:10 if i % 2 == 0]",
    ],
    "part-01/tutorial-01-05-dicts": [
        'books["Harry Potter and the Philosopher\'s Stone"] = "J.K. Rowling"',
        'books["1984"] = "Eric Blair"',
        "for (student, student_grades) in grades\n    averages[student] = sum(student_grades) / length(student_grades)\nend",
    ],
    "part-02/tutorial-02-01-functions": [
        "add(a, b) = a + b",
        ("replace", "# YOUR CHANGES BELOW\nfunction scope_test()\n    local_variable_one = 10\n    local_variable_two = 20\n    return local_variable_one\nend\n# YOUR CHANGES ABOVE"),
        "subtract(a, b) = a - b",
        ("replace", '# YOUR CHANGES BELOW\n@assert result1 == 30 "result1 should be the sum of two numbers"\n@assert result2 == "Hello, World!" "result2 should be the concatenation of two strings"\n@assert result3 == "Generic operation for objects of type String and Int64" "result3 should use the generic operation"\n# YOUR CHANGES ABOVE\nprintln("You solved it, the assertions are now correct!")'),
        "operation(a::Bool, b::Bool) = a && b",
    ],
    "part-02/tutorial-02-02-handling": [
        "import Pkg",
        'Pkg.add("DataFrames")',
        ("replace", '# YOUR CODE BELOW\nremove_command = "rm"'),
    ],
    "part-02/tutorial-02-03-DataFrames": [
        'employees = DataFrame(\n    Name = ["John", "Mike", "Frank"],\n    Age = [28, 23, 37],\n    Salary = [50000, 62000, 90000]\n)',
        "ages = employees.Age",
        "employees.Salary[1] = 59000",
        "high_earners = filter(row -> row.Salary > 60000, employees)",
        "sorted_df = sort(employees, :Age)",
        "employees.Bonus = zeros(nrow(employees))\nfor row in eachrow(employees)\n    if row.Age > 30\n        row.Bonus = 0.1 * row.Salary\n    else\n        row.Bonus = 0.05 * row.Salary\n    end\nend",
        "Overtime = DataFrame(\n    Name = String[],\n    ExtraHours = Int[]\n)\nfor row in eachrow(employees)\n    if row.Salary > 60000\n        push!(Overtime, (Name = row.Name, ExtraHours = 5))\n    else\n        push!(Overtime, (Name = row.Name, ExtraHours = 10))\n    end\nend",
    ],
    "part-02/tutorial-02-04-IO": [
        'read_matrix = readdlm("$(@__DIR__)/ExampleData/matrix.csv", \',\')',
        "CSV.write(csv_file_path, data)",
        'read_data = CSV.read("$(@__DIR__)/ExampleData/table_out.csv", DataFrame)',
        'orders_path = "$(@__DIR__)/ExampleData/orders.csv"\n# Read plainly, the crates column is text: "60,0" is not a number for CSV.read()\nprintln(CSV.read(orders_path, DataFrame))\norders = CSV.read(orders_path, DataFrame; delim=\';\', decimal=\',\')',
        "using Statistics\nunique!(orders)\n# Week 6 stays: its note says the harbour festival was real\norders.crates = coalesce.(orders.crates, median(skipmissing(orders.crates)))",
    ],
    "part-02/tutorial-02-05-Plotting": [
        'x = 1:20\ny = rand(20)\nscatter_plot = scatter(\n    x, y,\n    title="My First Scatter Plot",\n    xlabel="X-axis",\n    ylabel="Y-axis",\n    legend=false\n)',
        'x = 1:30\ny = rand(30)\ncustom_line_plot = plot(\n    x, y,\n    title="Customized Line Plot",\n    xlabel="X-axis",\n    ylabel="Y-axis",\n    line=(:dot, 1),\n    color=:blue,\n    marker=(:star, 3)\n)',
        'x = 1:30\ny1 = rand(30)\ny2 = rand(30)\ny3 = rand(30)\nmulti_series_plot = plot(\n    x, y1, label="Series A"\n)\nplot!(multi_series_plot, x, y2, label="Series B")\nplot!(multi_series_plot, x, y3, label="Series C")',
        'savefig(multi_series_plot, "$(@__DIR__)/ExampleData/saved_plot.png")',
    ],
    "part-03/tutorial-03-01-jump": [
        "@variable(model, productA >= 0)\n@variable(model, productB >= 0)",
        "@constraint(model, cutting_constraint, 2 * productA + 4 * productB <= 40)\n@constraint(model, finishing_constraint, 4 * productA + 3 * productB <= 60)",
        "@objective(model, Max, 100 * productA + 150 * productB)",
    ],
    "part-03/tutorial-03-02-bounds": [
        "@variable(model, water_amount)\n@variable(model, cars_produced, Int)\n@variable(model, build_store, Bin)",
        "@variable(model, daily_production[1:7] >= 0)",
        "@variable(model, stock_decision[1:3, 1:4], Bin)",
        "@variable(model, 0 <= temperature <= 37)",
    ],
    "part-03/tutorial-03-03-constraints": [
        "@variable(another_model, production[1:8] >= 0)\n@objective(another_model, Max, sum(margin[i] * production[i] for i in 1:8))",
        "@constraint(another_model, maxCapacity[i in 1:8], production[i] <= 12)",
        "@constraint(another_model, limitedDemand[i in 1:8; i <= 4], production[i] <= 5)",
    ],
    "part-03/tutorial-03-04-advanced": [
        'set_time_limit_sec(model, 120)\nset_optimizer_attribute(model, "mip_rel_gap", 0.005)\nset_optimizer_attribute(model, "presolve", "off")',
        '\n# Define variables\n@variable(model, widgets >= 0, Int)\n@variable(model, gadgets >= 0, Int)\n\n# Define constraints\n# We now have 300 minutes of production time available\n@constraint(model,\n    production_time,\n    2*widgets + 3*gadgets <= 300\n)\n@constraint(model,\n    widget_demand,\n    widgets <= 80\n)\n@constraint(model,\n    gadget_demand,\n    gadgets <= 60\n)\n\n# Define objective (profit), widgets now earn 30\n@objective(model,\n    Max,\n    30*widgets + 30*gadgets\n)\n\n# Solve the problem\noptimize!(model)\n\n# Print results\nprintln("Optimization status: ", termination_status(model))\nprintln("Objective value: ", objective_value(model))\nprintln("Widgets to produce: ", value(widgets))\nprintln("Gadgets to produce: ", value(gadgets))',
    ],
    "part-03/tutorial-03-05-transport": [
        "num_warehouses = nrow(available)\nnum_solar_farms = nrow(requested)",
        "transport_model = Model(HiGHS.Optimizer)",
        "@objective(transport_model, Max,\n    sum((revenue - varCosts - travelCosts_dict[(i,j)]) * X[i,j]\n    for i in keys(available_dict), j in keys(requested_dict))\n)",
        "@constraint(transport_model,\n    restrictAvailable[i in keys(available_dict)],\n    sum(X[i,j] for j in keys(requested_dict)) <= available_dict[i]\n)",
        "@constraint(transport_model,\n    restrictDemand[j in requested.solar_farm],\n    sum(X[i,j] for i in available.supplier) <= requested_dict[j]\n)",
        "optimize!(transport_model)",
        "total_delivered = sum(transport_df.truckloads)",
    ],
}

for rel, solutions in SOLUTIONS.items():
    nb = jupytext.read(SITE / f"{rel}.ipynb")
    todo = [c for c in nb.cells if c.cell_type == "code"
            and any(m in c.source for m in ("YOUR CODE BELOW", "YOUR CHANGES BELOW", "YOUR ANSWERS BELOW"))]
    assert len(todo) == len(solutions), f"{rel}: {len(todo)} exercise cells, {len(solutions)} solutions"
    for cell, solution in zip(todo, solutions):
        if isinstance(solution, tuple):
            cell.source = solution[1]
        else:
            cell.source = cell.source.rstrip() + "\n" + solution
    part, name = rel.split("/")
    target = OUT / part / "solution" / name
    target.parent.mkdir(parents=True, exist_ok=True)
    jupytext.write(nb, f"{target}.jl", fmt="jl:percent")
    jupytext.write(nb, f"{target}.ipynb")
    print(f"{rel}: {len(solutions)} exercises solved")

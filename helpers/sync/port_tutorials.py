"""Port the 15 Applied-Optimization twin tutorials into this workshop.

Each workshop tutorial becomes: its own front matter (title text taken from
the twin, numbering remapped) + the twin's body with the course-specific spots
adapted. Every adaptation must match exactly once, otherwise the script stops:
then the twin's wording changed and the adaptation below needs an update.
Writes to an output folder, never into the repos. Running it on tutorials that
are already ported reproduces them unchanged.

A full sync, from the repo root (needs the sibling checkout
../Applied-Optimization):

    python3 helpers/sync/port_tutorials.py /tmp/owj-port
    diff -r /tmp/owj-port/part-01 part-01 | less          # review, then copy over
    uv run quarto render                                  # tutorial notebooks in _site
    uv run python helpers/sync/build_solutions.py _site /tmp/owj-solutions
    bash helpers/sync/test_solutions.sh /tmp/owj-solutions  # 15 x PASS, then copy over
"""
import re
import sys
from pathlib import Path

OWJ = Path(__file__).resolve().parents[2]
AO = OWJ.parent / "Applied-Optimization" / "tutorials"
OUT = Path(sys.argv[1])

PAIRS = {
    "02-01-variables": "part-01/tutorial-01-01-variables",
    "02-02-vectors": "part-01/tutorial-01-02-vectors",
    "02-03-comparisons": "part-01/tutorial-01-03-comparisons",
    "02-04-loops": "part-01/tutorial-01-04-loops",
    "02-05-dicts": "part-01/tutorial-01-05-dicts",
    "03-01-functions": "part-02/tutorial-02-01-functions",
    "03-02-handling": "part-02/tutorial-02-02-handling",
    "03-03-DataFrames": "part-02/tutorial-02-03-DataFrames",
    "03-04-IO": "part-02/tutorial-02-04-IO",
    "03-05-Plotting": "part-02/tutorial-02-05-Plotting",
    "04-01-jump": "part-03/tutorial-03-01-jump",
    "04-02-bounds": "part-03/tutorial-03-02-bounds",
    "04-03-constraints": "part-03/tutorial-03-03-constraints",
    "04-04-advanced": "part-03/tutorial-03-04-advanced",
    "04-05-transport": "part-03/tutorial-03-05-transport",
}
ROMAN = {"II": "I", "III": "II", "IV": "III"}
INCLUDE = "{{< include ../include/activate_environment.qmd >}}\n\n"


def split(text):
    """Front matter (without the --- lines) and body."""
    assert text.startswith("---\n")
    end = text.index("\n---\n", 4)
    return text[4:end], text[end + 5:]


def rep(body, old, new, name):
    assert body.count(old) == 1, f"{name}: expected exactly one match for {old[:60]!r}, found {body.count(old)}"
    return body.replace(old, new)


def between(text, start, end):
    i = text.index(start)
    return text[i:text.index(end, i)]


for ao_name, owj_rel in PAIRS.items():
    ao_fm, body = split((AO / f"tutorial-{ao_name}.qmd").read_text())
    owj_text = (OWJ / f"{owj_rel}.qmd").read_text()
    owj_fm, owj_body = split(owj_text)
    owj_stem = Path(owj_rel).name

    # front matter: the workshop's own, title text from the twin
    num, sub, text = re.search(r'^title: "Tutorial (\w+)\.(\w+) - (.*)"$', ao_fm, re.M).groups()
    owj_fm, n = re.subn(r'^title: .*$', f'title: "Tutorial {ROMAN[num]}.{sub} - {text}"', owj_fm, flags=re.M)
    assert n == 1, ao_name

    # the twin activates its environment through an include; the workshop
    # renders against the root Project.toml
    body = rep(body, INCLUDE, "", ao_name)
    body = body.replace(f"tutorial-{ao_name}", owj_stem)
    body = re.sub(r"Tutorial (II|III|IV)\.(?=[IVX])", lambda m: f"Tutorial {ROMAN[m.group(1)]}.", body)

    if ao_name == "02-01-variables":
        end = "\n---\n\n# Section 1 - Variables"
        ao_block = between(body, "## Julia in Zed\n", end)
        owj_block = between(owj_body, "## Julia in Zed\n", end)
        body = rep(body, ao_block, owj_block, ao_name)

    if ao_name == "02-04-loops":
        body = rep(body, "When you run the cells one by one in Zed, the following",
                   "When you run the cells one by one in Zed or in a notebook, the following", ao_name)

    if ao_name == "03-02-handling":
        body = rep(body, "There, we created the course environment in the folder `applied-optimization` inside your course folder.",
                   "There, we created the workshop environment in the folder `optimization-workshop` inside your workshop folder.", ao_name)
        body = rep(body, 'Pkg.activate("applied-optimization")', 'Pkg.activate("optimization-workshop")', ao_name)
        body = rep(body, "Here, `\"applied-optimization\"` is the path to the folder with the course's `Project.toml`, relative to the folder Julia runs in: your course folder.",
                   "Here, `\"optimization-workshop\"` is the path to the folder with the workshop's `Project.toml`, relative to the folder Julia runs in: your workshop folder.", ao_name)
        body = rep(body, 'Our Zed kernel "Applied Optimization" from the first tutorial already starts in this environment. Therefore, we don\'t need to activate it most of the time: in Zed, `Pkg.add` installs packages into the course environment directly.',
                   'Our kernel "Optimization with Julia" from the first tutorial already starts in this environment. Therefore, we don\'t need to activate it most of the time: `Pkg.add` installs packages into the workshop environment directly.', ao_name)

    if ao_name == "03-04-IO":
        # DelimitedFiles is not in the workshop's package list; it loads as a
        # standard library (checked with Julia 1.13.1), as the workshop said
        body = rep(body, "The DelimitedFiles package ships with the course environment, so you can use it right away in this course. In your own projects, you first have to add it with `Pkg.add(\"DelimitedFiles\")`, just like any other package.",
                   "The DelimitedFiles package is part of Julia's Standard Library, which means you can use it without installing anything extra!", ao_name)
        body = rep(body, "Remember the brewery game from the lecture? Its order file now lands on your desk.",
                   "The order file of a brewery lands on your desk.", ao_name)
        body = rep(body, " and read `60,0` as 600: that is what happened in the game.", " and read `60,0` as 600.", ao_name)
        body = rep(body, "::: {.callout-note}\nThis is the same file as in the lecture's game. In lecture 5, these weekly orders become the demand of the brewery's production model, there in bottles: 20 per crate.\n:::\n\n", "", ao_name)

    if ao_name == "03-05-Plotting":
        # the include also carried the Plots figure fix; the workshop has it inline
        fix = between(owj_body, "```{julia}\n#| echo: false\n#| output: false\n# Plots.jl otherwise", "# Introduction")
        assert "package_callbacks" in fix
        body = rep(body, "# Introduction\n", fix + "# Introduction\n", ao_name)

    if ao_name == "04-01-jump":
        body = rep(body, "In the lecture's game, the two products are skateboards (product A) and surfboards (product B): the same workshop, with the same numbers.\n\n", "", ao_name)

    if ao_name == "04-04-advanced":
        body = rep(body, "it becomes important for sensitivity analysis later in the course.", "it becomes important for sensitivity analysis.", ao_name)

    if ao_name == "04-05-transport":
        body = rep(body, "It is the profit maximization model from the end of the first lecture:", "It is a profit maximization model:", ao_name)
        body = rep(body, " This is the profit maximization model from the end of the first lecture - but this time with real data.", "", ao_name)
        body = rep(body, " Remember the discussion from the first lecture, where we changed the demand constraint from \"meet the demand exactly\" to \"deliver at most the demand\" for exactly this reason.", "", ao_name)
        # the data sets are linked on the page, as in the twin
        if "data/cost.csv" not in owj_fm:
            owj_fm = rep(owj_fm, f"    href: {owj_stem}.jl",
                         f"    href: {owj_stem}.jl\n"
                         "  - text: Panels\n    icon: filetype-csv\n    href: data/available-panels.csv\n"
                         "  - text: Demand\n    icon: filetype-csv\n    href: data/panel-demand.csv\n"
                         "  - text: Costs\n    icon: filetype-csv\n    href: data/cost.csv", ao_name)

    leftovers = re.findall(r"[^\n]*(?:applied-optimization|Applied Optimization|lecture|tutorial-0[2-9]-0)[^\n]*", body, flags=re.I)
    assert not leftovers, f"{ao_name}: course-specific text left: {leftovers}"

    target = OUT / f"{owj_rel}.qmd"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(f"---\n{owj_fm}\n---\n{body}")
    print(f"{ao_name:20s} -> {owj_rel}.qmd")

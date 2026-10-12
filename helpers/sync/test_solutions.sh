#!/usr/bin/env bash
# Run every solution as a script: all @assert tests of a tutorial must pass.
#
#   bash helpers/sync/test_solutions.sh [folder holding part-0X/solution/*.jl]
#
# Without an argument it tests the solutions in the repo. It runs in a
# temporary folder with a copy of the Julia environment, so the tutorials'
# Pkg.add cells and the files they write never touch the repo.
set -u
REPO="$(cd "$(dirname "$0")/../.." && pwd)"
SRC="${1:-$REPO}"
RUN="$(mktemp -d)"
mkdir "$RUN/env" && cp "$REPO/Project.toml" "$REPO/Manifest.toml" "$RUN/env/"
for part in part-01 part-02 part-03; do
    mkdir -p "$RUN/$part"
    cp "$SRC/$part/solution/"*.jl "$RUN/$part/"
    # the tutorials read their data next to the file
    [ -d "$REPO/$part/data" ] && cp -R "$REPO/$part/data" "$RUN/$part/data"
done
# the functions tutorial shows one line that is meant to fail (a local variable
# used outside its function); skip it in the run copy only
sed -i.bak 's/^println(secret_ingredient)$/# &/' "$RUN/part-02/tutorial-02-01-functions.jl"
run_one() {
    f="$1"; dir=$(dirname "$f")
    # GKSwstype: Plots must not try to open a window
    if (cd "$dir" && GKSwstype=100 julia --startup-file=no --project="$RUN/env" "$(basename "$f")" > "$f.log" 2>&1); then
        echo "PASS $(basename "$f")"
    else
        echo "FAIL $(basename "$f")   log: $f.log"
    fi
}
export -f run_one; export RUN
results="$(find "$RUN" -name "tutorial-*.jl" | sort | xargs -P 4 -I{} bash -c 'run_one {}' | sort)"
echo "$results"
! grep -q "^FAIL" <<< "$results"

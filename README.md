# Collatz

This repository contains a Python script to generate a Graphviz DOT file
visualizing a simple Collatz tree. The graph is directed with edges pointing
toward the trunk node `1`. Nodes are drawn as circles and edges are straight
lines.

## Usage

Run the script to produce `collatz_tree.dot`:

```bash
python3 collatz_tree.py --depth 10 -o collatz_tree.dot
```

The depth option controls how many trunk nodes of the form `1 * 2^x` are
included. Branches are only added from trunk nodes where `x` is even and at
least `4` (starting with `16`). These branches connect to the value
`1 * (2^(2x))` and are drawn horizontally to form right angles with the trunk.

To render the resulting DOT file to an image you need Graphviz installed. For
example:

```bash
dot -Tpng collatz_tree.dot -o collatz_tree.png
```

This will create `collatz_tree.png` showing a trunk with branches drawn at right
angles.

#!/usr/bin/env python3
"""Generate a Graphviz DOT file describing a Collatz tree visualization.

This script builds a directed graph where edges point toward the trunk node 1.
It places trunk nodes along a vertical axis and branch nodes horizontally so
that each branch forms a right angle with the trunk. The output DOT text can
be rendered with Graphviz to produce an image.
"""

import argparse


def generate_collatz_tree(max_depth: int) -> str:
    """Return a DOT representation for the Collatz tree up to ``2**max_depth``."""
    lines = [
        "digraph CollatzTree {",
        "    graph [splines=line]",  # keep edges straight
        "    node [shape=circle]"  # draw nodes as circles
    ]

    # Trunk nodes starting at 1 (2**0)
    for x in range(0, max_depth + 1):
        node_val = 2 ** x
        # Position along the vertical axis (x=0) so trunk is vertical
        lines.append(f'    "{node_val}" [pos="0,{x}!" label="{node_val}"]')
        if x > 0:
            parent = 2 ** (x - 1)
            # Edge direction toward 1
            lines.append(f'    "{node_val}" -> "{parent}"')

    # Branches at right angles from trunk nodes
    for x in range(1, max_depth + 1):
        trunk_val = 2 ** x
        branch_val = 2 ** (2 * x)
        # Place branch horizontally to the right of the trunk
        lines.append(f'    "{branch_val}" [pos="{x},{x}!" label="{branch_val}"]')
        # Edge directed toward the trunk
        lines.append(f'    "{branch_val}" -> "{trunk_val}"')

    lines.append("}")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a Collatz tree DOT file")
    parser.add_argument(
        "--depth",
        type=int,
        default=10,
        help="Maximum exponent for trunk nodes (default: 10)",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default="collatz_tree.dot",
        help="Output DOT filename",
    )
    args = parser.parse_args()

    dot_text = generate_collatz_tree(args.depth)
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(dot_text)
    print(f"DOT file written to {args.output}")


if __name__ == "__main__":
    main()

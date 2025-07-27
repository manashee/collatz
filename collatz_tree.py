#!/usr/bin/env python3
"""Generate a Graphviz DOT file describing a Collatz tree visualization.

This script builds a directed graph where edges point toward the trunk node 1.
It places trunk nodes along a vertical axis and branch nodes horizontally so
that each branch forms a right angle with the trunk. The output DOT text can
be rendered with Graphviz to produce an image.
"""

import argparse

def trunk_child_node(parent: str) -> str:
    """Creates a child node in the trunk of an existing node - parent.
    Use case: how to add
    """
    return ""

def generate_collatz_tree(max_depth: int) -> str:
    """Return a DOT representation for the Collatz tree up to ``2**max_depth``.

    Branches are only added from trunk nodes where the exponent is even and at
    least four (e.g. from 16, 64, 256, ...). Each branch points horizontally
    toward its trunk node so that the edge forms a right angle with the trunk.
    """
    lines = [
        "digraph CollatzTree {",
        "    graph [splines=line layout=neato len=1.0]",  # keep edges straight, use neato engine, constant edge length
        "    node [shape=circle]"  # draw nodes as circles
    ]

    # Trunk nodes starting at 1 (2**0)
    for x in range(0, max_depth + 1):
        node_val = 2 ** x
        # print(node_val)
        # Position along the vertical axis (x=0) so trunk is vertical
        lines.append(f'    "{node_val}" [pos="0,{x}!" label="{node_val}"]')
        if x > 0:
            parent = 2 ** (x - 1)
            # Edge direction toward 1
            lines.append(f'    "{node_val}" -> "{parent}"')

    # Branches at right angles from trunk nodes with even exponent >= 4
    branch_count = 1  # Counter for unique branch node labels
    for x in range(4, max_depth + 1, 2):
        trunk_val = 2 ** x

        # Calculate branch value using formula ((2^(2x)) - 1) / 3
        branch_val = (2 ** x - 1) // 3
        
        # Calculate edge length that doubles as loop progresses
        edge_length = 2 ** (branch_count - 1)
        
        # Add a node with calculated value to the right of the trunk at the same y
        # Position horizontally to the right of trunk at same y-coordinate for 90-degree angle
        lines.append(f'    "{branch_val}" [pos="{x//2},{x}!" label="{branch_val}"]')
        # Edge directed toward the trunk with increasing length
        lines.append(f'    "{branch_val}" -> "{trunk_val}" [len={edge_length}]')
        branch_count += 1

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

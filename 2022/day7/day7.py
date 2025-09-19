from typing import Any

from anytree import Node, PostOrderIter, PreOrderIter

with open("day7/input.txt", "r") as f:
    input: list[str] = f.readlines()


file_tree: Any = Node("root", node_size=0)
current_node: Any = file_tree


for line in input:
    if line.startswith("$ cd"):
        dir = line.split()[-1]
        if dir == "..":
            current_node = current_node.parent
        elif dir != "/":
            current_node = Node(dir, parent=current_node, node_size=0)

    elif not line.startswith("dir") and not line.startswith("$ ls"):
        size, name = line.split()
        current_node.children += (Node(name, node_size=int(size)),)


for node in PostOrderIter(file_tree):
    parent = node.parent
    if parent is not None:
        parent.node_size += node.node_size

print(
    "Part 1:",
    sum(
        node.node_size
        for node in PreOrderIter(file_tree)
        if len(node.children) > 0 and node.node_size <= 100000
    ),
)

TOTAL_SPACE = 70000000
REQUIRED_SPACE = 30000000

free_space = TOTAL_SPACE - file_tree.node_size
required_deletion = REQUIRED_SPACE - free_space

print(
    "Part 2:",
    min(
        node.node_size
        for node in PreOrderIter(file_tree)
        if len(node.children) > 0 and node.node_size >= required_deletion
    ),
)

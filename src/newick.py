"""A Newick parser."""

from __future__ import annotations
from dataclasses import dataclass
from typing import Union, cast
import re


def tokenize(tree: str) -> list[str]:
    """
    Extract the tokens from the text representation of a tree.

    >>> tokenize("A")
    ['A']
    >>> tokenize("(A, (B, C))")
    ['(', 'A', '(', 'B', 'C', ')', ')']
    """
    return re.findall(r'[()]|\w+', tree)


@dataclass(repr=False)
class Leaf:
    """
    A leaf in a tree.

    This will just be a string for our application.
    """

    name: str

    def __str__(self) -> str:
        """Simplified text representation."""
        return self.name
    __repr__ = __str__


@dataclass(repr=False)
class Node:
    """An inner node."""

    children: list[Tree]

    def __str__(self) -> str:
        """Simplified text representation."""
        return f"({','.join(str(child) for child in self.children)})"
    __repr__ = __str__


# A tree is either a leaf or an inner node with sub-trees
Tree = Union[Leaf, Node]


def parse(tree: str) -> Tree:
    """
    Parse a string into a tree.

    >>> parse("(A, (B, C))")
    (A,(B,C))
    """
    stack = list()
    for x in tokenize(tree):
        if x == "(":
            stack.append(x)
        elif x == ")":
            new_branch = list()
            leaf = stack.pop()
            while leaf != "(":
                new_branch.append(leaf)
                leaf = stack.pop()
            new_branch.reverse()
            stack.append(Node(new_branch))
        else:
            stack.append(Leaf(x))
    return stack.pop()

print(parse("((A, B), C, ((D, E), F))"))
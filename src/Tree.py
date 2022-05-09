from __future__ import annotations
from typing import List
from src.Table import Table


class Tree:
    root: Node
    level: int

    def __init__(self, level: int):
        pass


class Node:

    def __init__(self, array):
        self.array = array

    label: str  # aktualna wartosc atrybutu
    decision_table: Table  # tablica
    children: List[Node]
    branch_label: str  # wartosc atrybutu z ktorego zostala stworzona typu old, mid, new

    def __init__(self, branch_label: str, decision_table: Table):
        self.branch_label = branch_label
        self.decision_table = decision_table
        self.children = []

    def __int__(self, label: str, branch_label: str):
        self.label = label
        self.branch_label = branch_label
        self.children = []

    def add_child(self, child: Node):
        self.children.append(child)

    def get_children(self, children):
        return children

    def get_table(self):
        return self.decision_table

    def set_label(self, label: str):
        self.label = label

    def get_label(self):
        return self.label

    def set_branch_label(self, branch_label: str):
        self.branch_label = branch_label

    def get_branch_label(self):
        return self.branch_label

    def is_leaf(self) -> bool:
        return True if self.children else False

    def is_root(self) -> bool:
        return self.branch_label == 1

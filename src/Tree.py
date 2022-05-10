from __future__ import annotations

from dataclasses import dataclass
from typing import List
from src.Table import Table


@dataclass
class Node:
    label: int  # aktualna wartosc atrybutu
    branch_label: str  # wartosc atrybutu z ktorego zostala stworzona typu old, mid, new
    table: Table  # tablica
    children: List[Node]
    indent: int
    parent_label: str

    def __init__(self, label: str, branch_label: str, table: Table, children: List[Node], indent: int):
        self.label = label
        self.branch_label = branch_label
        self.table = table
        self.children = children
        self.indent = indent + 1

    def __str__(self):
        return {
            'Label: ': self.label,
            'Branch label: ': self.branch_label,
            #'Table: ': self.table.table,
            'Children: ': [children.__str__() for children in self.children],
            'Indent: ': self.indent
        }

    # def __init__(self, branch_label: str, decision_table: Table):
    #     self.branch_label = branch_label
    #     self.decision_table = decision_table
    #     self.children = []
    #
    # def __int__(self, label: str, branch_label: str):
    #     self.label = label
    #     self.branch_label = branch_label
    #     self.children = []

    def get_children(self, children):
        return children

    def get_table(self):
        return self.decision_table

    def get_label(self):
        return self.label

    def get_branch_label(self):
        return self.branch_label

    def get_decision_attr(self):
        return self.table.table[0][-1]

    def is_leaf(self) -> bool:
        return False if len(self.children) == 0 else True

    def is_root(self) -> bool:
        return self.branch_label == 'root'


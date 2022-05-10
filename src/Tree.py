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
    index: int

    def __init__(self, label: str, branch_label: str, table: Table, children: List[Node], index: int):
        self.label = label
        self.branch_label = branch_label
        self.table = table
        self.children = []
        self.index = index

    def __str__(self):
        return {
            "label: ": self.label,
            "branch label: ": self.branch_label,
            #"table: ": self.table.table,
            "children: ": [children.__str__() for children in self.children],
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

    def get_table(self):
        return self.decision_table

    def get_label(self):
        return self.label

    def get_branch_label(self):
        return self.branch_label

    def is_leaf(self) -> bool:
        return True if self.children else False

    def is_root(self) -> bool:
        return self.branch_label == 'root'

    def get_attrs(self):
        dict_of_attrs = {}

        for row in self.table.table:
            dict_of_attrs[row[self.label]] = row[-1]

        return dict_of_attrs

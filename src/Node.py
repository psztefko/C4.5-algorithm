from __future__ import annotations

from dataclasses import dataclass
from typing import List
from src.Table import Table


@dataclass
class Node:
    label: int
    branch_label: str
    table: Table
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

    def is_leaf(self) -> bool:
        return True if self.children else False

    def is_root(self) -> bool:
        return self.branch_label == 'root'

    def get_attrs(self):
        """
        Creates dict of conditional attribute as key and it's decision attribute as value
        :return:
        """
        dict_of_attrs = {}

        for row in self.table.table:
            dict_of_attrs[row[self.label]] = row[-1]

        return dict_of_attrs

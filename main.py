import csv
from typing import List
from src.Table import Table
from src.Node import Node


def load_data(path: str) -> List[List[any]]:
    """
    Load data from file
    :return list of list of values
    """
    data = []
    with open(path, newline="") as file:
        csv_reader = csv.reader(file, delimiter=",")
        for row in csv_reader:
            data.append(row)

    return data


def build(node: Node):
    """
    Creates tree made using recurrence
    :param node:
    :return:
    """
    array = node.table

    index = array.get_highest_gain_ratio_index()

    if index != -1:
        tables = []
        for key in list(array.occurrences_array[index].keys()):
            tables.append(Table([row for row in array.table if row[index] == key]))

        for table in tables:
            node.children.extend([Node(index, table.table[0][index], table, [], index)])

        for child in node.children:
            build(child)


def print_tree(node: Node, indent=0):
    """
    Prints tree structure
    :param node:
    :param indent:
    :return:
    """
    if node.is_root():
        print_root(node.label)
        for n in node.children:
            print_tree(n, indent + 2)
    elif node.children:
        print_node(node.branch_label, node.children[0].index, indent)
        for n in node.children:
            print_tree(n, indent + 2)
    else:
        print_leaf(node, indent)

    return dict


def print_leaf(node: Node, indent):
    for key, value in node.get_attrs().items():
        print('  '*indent + key + ' -> ' + value)


def print_root(label):
    print('Atrybut ', label)


def print_node(branch_label: str, index: int, indent: int):
    print('  '*indent + branch_label + ' -> ' + 'Atrybut ' + str(index))


array = load_data("data/breast-cancer.data")

node = Node(0, "root", Table(array), [], None)

build(node)

print_tree(node)

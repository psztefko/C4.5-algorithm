import csv
from typing import List
from src.Table import Table
from src.Tree import Node


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
    array = node.table

    index = array.get_highest_gain_ratio_index()

    if index != -1:
        tables = []
        for key in list(array.occurrences_array[index].keys()):
            tables.append(Table([row for row in array.table if row[index] == key]))

            # print(new_table.table)
            # print(new_table.get_highest_gain_ratio_index())

        for table in tables:
            node.children.extend([Node(index, table.table[0][index], table, [])])

        for child in node.children:
            build(child)

    else:  # zostaje liściem
        pass


array = load_data("gielda.txt")

node = Node(0, "root", Table(array), [])
build(node)

print(node.__str__())
# {1: {'old': 'down', 'mid': {2: {'yes': 'down', 'no': 'up'}}, 'new': 'up'}}

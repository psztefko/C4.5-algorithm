import csv
from typing import List
from src.Table import Table
from src.Tree import Node, Tree


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


def build(array: List[any], attr: str, intend=''):

    index = array.get_highest_gain_ratio_index()

    if index >= 0:
        attr = 'a' + str(index + 1)
        intend += '    '
        print(intend + attr)
    else:
        pass
        # intend = intend[:-4]

    if (index != -1):
        for key in list(array.occurrences_array[index].keys()):
            new_array = Table([row for row in array.table if row[index] == key])
            # print(new_array.table)
            # print(new_array.get_highest_gain_ratio_index())

            print(intend + ': ' + str(key) + ' -> ' + str(new_array.table[0][new_array.columns - 1]))
            build(new_array, attr, intend)

    else:  # zostaje liściem
        pass


build(Table(load_data("car.data")), '')

# {1: {'old': 'down', 'mid': {2: {'yes': 'down', 'no': 'up'}}, 'new': 'up'}}

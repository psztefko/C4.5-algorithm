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



def build(array: List[any]):
    #node = Node()
    print('--')
    index = array.get_highest_gain_ratio_index()
    if(index != -1):
        for key in list(array.occurrences_array[index].keys()):
            new_array = Table([row for row in array.table if row[index] == key])
            print(new_array.table)
            print(new_array.get_highest_gain_ratio_index())

            build(new_array)

    else: # zostaje liściem
        pass



build(Table(load_data("gielda.txt")))



# {1: {'old': 'down', 'mid': {2: {'yes': 'down', 'no': 'up'}}, 'new': 'up'}}

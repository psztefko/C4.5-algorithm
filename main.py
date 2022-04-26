import csv
from typing import List
from math import log2


def load_data(path: str) -> List[List[int]]:
    """ "GIT"""
    conditional_attributes = []
    with open(path, newline="") as file:
        csv_reader = csv.reader(file, delimiter=",")
        for row in csv_reader:
            conditional_attributes.append(row)

    return conditional_attributes


def extract_columns(conditional_attributes: List[List[int]]) -> List[List[int]]:
    """GIT"""
    columns = []
    for column_index in range(len(conditional_attributes[0])):
        column = []
        for row_index in range(len(conditional_attributes)):
            column.append(conditional_attributes[row_index][column_index])
        columns.append(column)

    return columns


def create_dictionary_of_values(column: List[int]) -> dict:
    """GIT"""
    dictionary_of_values = {}

    for attribute in column:
        if attribute in dictionary_of_values:
            dictionary_of_values[attribute] += 1
        else:
            dictionary_of_values[attribute] = 0

    return dictionary_of_values

def get_class_occurances(columns):
    return [create_dictionary_of_values(column) for column in columns]

conditional_attributes = load_data("test2.txt")

columns = extract_columns(conditional_attributes)


list_of_dicts = get_class_occurances(columns)
print(list_of_dicts)
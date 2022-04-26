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
            dictionary_of_values[attribute] = 1

    return dictionary_of_values


def get_class_occurrences(columns):
    """GIT"""
    return [create_dictionary_of_values(column) for column in columns]


def count_probability(conditional_attribute_dict: dict, column_length: int) -> List[float]:
    return [element / column_length for element in conditional_attribute_dict.values()]


conditional_attributes = load_data("gielda.txt")

# convert list of rows to list of columns
columns = extract_columns(conditional_attributes)

decisional_attribute = columns[-1]
columns = columns[:-1]

# get dict of values and their occurrences for each attribute
list_of_dicts = get_class_occurrences(columns)

list_of_probabilities = []
for dictionary in list_of_dicts:
    list_of_probabilities.append(count_probability((dictionary), len(columns[0])))



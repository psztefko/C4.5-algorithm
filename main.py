import csv
from typing import List, Dict
from math import log2


def load_data(path: str) -> List[List[any]]:
    """Load data from file
        :return list of list of values
    """
    data = []
    with open(path, newline="") as file:
        csv_reader = csv.reader(file, delimiter=",")
        for row in csv_reader:
            data.append(row)

    return data


def extract_columns(conditional_attributes: List[List[int]]) -> List[List[int]]:
    """Converts list of rows to list of columns
        :return list of columns
    """
    columns = []
    for column_index in range(len(conditional_attributes[0])):
        column = []
        for row_index in range(len(conditional_attributes)):
            column.append(conditional_attributes[row_index][column_index])
        columns.append(column)

    return columns


def get_class_occurrences(column: List[int]) -> Dict[any, int]:
    """Creates dictionary with each column value as a key and its occurrence as value
        :return dict{"value": occurrence}
    """
    dictionary_of_values = {}

    for attribute in column:
        if attribute in dictionary_of_values:
            dictionary_of_values[attribute] += 1
        else:
            dictionary_of_values[attribute] = 1

    return dictionary_of_values


def get_classes_occurrences(columns: List[List[int]]) -> List[Dict[str, int]]:
    """Get dict with values occurrence for each column
        :return list of dictionaries
    """
    return [get_class_occurrences(column) for column in columns]


def count_probability(conditional_attribute_dict: dict, column_length: int) -> List[float]:
    """Count probability of each value in column
        :return list of probabilities
    """
    return [element / column_length for element in conditional_attribute_dict.values()]


def count_entropy(probabilities: List[float]) -> float:
    """Count entropy of column based on it's probabilities
        :return entropy
    """
    return -(sum([probability * log2(probability) for probability in probabilities]))


def information_func():
    pass

conditional_attributes = load_data("gielda.txt")

# convert list of rows to list of columns
columns = extract_columns(conditional_attributes)

decision_attribute = columns[-1]
columns = columns[:-1]

# get dict of values and their occurrences for each attribute
decision_attr_occurrence = get_class_occurrences(decision_attribute)

probabilities = count_probability(decision_attr_occurrence, len(columns[0]))

count_entropy(probabilities)

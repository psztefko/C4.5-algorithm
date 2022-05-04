from typing import List, Dict
from math import log2


class Array:
    array: List[List[any]]
    occurrences_array: List[Dict[str, int]]
    column_length: int
    row_length: int

    def __init__(self, array):
        self.array = array
        self.column_length = len(array)
        self.row_length = len(array[0])
        self.occurrences_array = self.get_occurrences()

    def get_occurrences(self):
        """Extract dict of classes occurrence for given index attribute
            :return dictionary of class and it's occurrence
        """

        occurrences_array = []
        for column_index in range(self.row_length):
            classes_occurrence = {}
            for row in self.array:
                attribute = row[column_index]
                if attribute in classes_occurrence:
                    classes_occurrence[attribute] += 1
                else:
                    classes_occurrence[attribute] = 1

            occurrences_array.append(classes_occurrence)

        return occurrences_array

    def get_probability(self, attr_index: int) -> List[float]:
        """Count probability of each value in column
            :return list of probabilities
        """
        return [element / self.column_length for element in self.occurrences_array[attr_index].values()]

    def get_entropy(self, attr_index: int):
        """Count entropy of column based on it's probabilities
            :return entropy
        """
        return -(sum([probability * log2(probability) for probability in self.get_probability(attr_index)]))

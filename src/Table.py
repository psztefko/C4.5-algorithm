from typing import List, Dict
from math import log2


class Table:
    table: List[List[any]]
    occurrences_array: List[Dict[str, int]]
    rows: int
    columns: int

    def __init__(self, array):
        self.table = array
        self.rows = len(array)
        self.columns = len(array[0])
        self.occurrences_array = self.occurrences()

    def occurrences(self):
        """
        Extract dict of classes occurrence for given index attribute
        :return dictionary of class and it's occurrence
        """

        occurrences_array = []
        for column_index in range(self.columns):
            classes_occurrence = {}
            for row in self.table:
                attribute = row[column_index]
                if attribute in classes_occurrence:
                    classes_occurrence[attribute] += 1
                else:
                    classes_occurrence[attribute] = 1

            occurrences_array.append(classes_occurrence)

        return occurrences_array

    def probability(self, attr_index: int) -> List[float]:
        """
        Count probability of each value in column
        :return list of probabilities
        """
        return [element / self.rows for element in self.occurrences_array[attr_index].values()]

    def entropy(self, attr_index: int):
        """
        Count entropy of column based on it's probabilities
        :return entropy
        """
        return -(sum([probability * log2(probability) for probability in self.probability(attr_index)]))

    def information(self, attr_index: int):
        """
        Count information func value for given attribute
        :return
        """

        attr_info = 0.0
        for key in self.occurrences_array[attr_index].keys():
            subset = Table([row for row in self.table if row[attr_index] == key])

            attr_info += subset.rows / self.rows * subset.entropy(self.columns - 1)

        return attr_info

    def gain(self, attr_index) -> float:
        """
        Count gain based on table entropy - attribute information func
        :param attr_index
        :return: gain
        """

        return self.entropy(self.columns - 1) - self.information(attr_index)

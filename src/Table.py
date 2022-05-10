from typing import List, Dict
from math import log2


class Table:
    table: List[List[any]]
    occurrences_array: List[Dict[str, int]]
    rows: int
    columns: int
    conditional_attrs: List[any]
    decisional_attrs = List[any]

    def __init__(self, array):
        self.table = array
        self.rows = len(array)
        self.columns = len(array[0])
        self.occurrences_array = self.occurrences()
        self.conditional_attrs = self.table[:-1]
        self.decisional_attrs = self.table[-1]

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
        return [
            element / self.rows
            for element in self.occurrences_array[attr_index].values()
        ]

    def entropy(self, attr_index: int) -> float:
        """
        Count entropy of column based on it's probabilities
        :return entropy
        """
        return -(
            sum(
                [
                    probability * log2(probability)
                    for probability in self.probability(attr_index)
                ]
            )
        )

    def custom_entropy(self, custom_table: List[any]) -> float:
        """
        Count entropy for a custom table of probabilities
        :param custom_table:
        :return:
        """
        return -(sum([probability * log2(probability) for probability in custom_table]))

    def information(self, attr_index: int) -> float:
        """
        Count information func value for given attribute
        :return attribute info
        """

        attr_info = 0.0
        for key in self.occurrences_array[attr_index].keys():
            sub_table = Table([row for row in self.table if row[attr_index] == key])

            attr_info += (
                sub_table.rows / self.rows * sub_table.entropy(self.columns - 1)
            )

        return attr_info

    def gain(self, attr_index) -> float:
        """
        Count gain based on table entropy - attribute information func
        :param attr_index
        :return: gain
        """

        return self.entropy(self.columns - 1) - self.information(attr_index)

    def split_information(self, attr_index: int) -> float:
        """
        Count entropy value for given attribute
        :param attr_index:
        :return:
        """

        probability = []
        for key in self.occurrences_array[attr_index].keys():
            sub_table = Table([row for row in self.table if row[attr_index] == key])

            probability.append(sub_table.rows / self.rows)

        return self.custom_entropy(probability)

    def gain_ratio(self, attr_index: int) -> float:
        """
        Count gain ratio based on gain and split information values
        :param attr_index:
        :return:
        """
        info = self.split_information(attr_index)
        return self.gain(attr_index) / info if info != 0 else 0

    def get_highest_gain_ratio_index(self) -> int:
        """
        Gets index of attribute with highest gain ratio
        :return: index
        """
        highest_gain_ratio = self.gain_ratio(0)
        highest_gain = 0
        for index in range(self.columns - 1):
            if self.gain_ratio(index) > highest_gain_ratio:
                highest_gain = index
                highest_gain_ratio = self.gain_ratio(index)

        if highest_gain_ratio > 0:
            return highest_gain
        else:
            return -1

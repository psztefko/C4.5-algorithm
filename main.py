import csv
from typing import List
from src.Array import Array


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

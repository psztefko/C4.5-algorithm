import csv


def load_data(path):
    list_of_rows = []
    with open(path, newline='') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            list_of_rows.append(row)
            #print(row)

    return list_of_rows


def identify_unique_classes(list_of_rows):
    temp = ''
    for row in list_of_rows:
        for char in row:
            temp += char
    uniques = set(temp)
    return uniques


def count_class_occurance(list_of_rows, uniques):
    dict = {}
    for unique in uniques:
        dict[unique] = 0

    for row in list_of_rows:
        for char in row:
            dict[char] += 1

    return dict

list_of_rows = load_data('test.txt')
count_class_occurance(list_of_rows, identify_unique_classes(list_of_rows))
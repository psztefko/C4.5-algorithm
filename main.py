import csv


def load_data(path):
    list_of_rows = []
    with open(path, newline='') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            list_of_rows.append(row)
            #print(row)

    return list_of_rows


def identify_and_count_unique_classes(list_of_rows):
    dict = {}
    for row in list_of_rows:
        for char in row:
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 0
    return dict


list_of_rows = load_data('test.txt')

print(identify_and_count_unique_classes(list_of_rows))

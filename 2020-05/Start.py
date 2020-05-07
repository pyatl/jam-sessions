import csv


def Easy(filename):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row)

    return 0


def Medium(filename):
    return []


def Hard(filename):
    return []

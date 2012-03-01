import csv
class CSVmaker:
    __file = None

    def __init__(self, file):
        self.__file = csv.writer(open(file, 'wb'))

    def write(self, list):
        self.__file.writerow(list)


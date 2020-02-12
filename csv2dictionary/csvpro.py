import io, csv

class CsvBrain(object):
    """docstring"""
    def __init__(self, csv_file):
        self.data = []
        with open(csv_file, mode='r', encoding='utf-8-sig') as f:
            self.csv_file = f.read()
        io_string = io.StringIO(self.csv_file)
        row_count = 0
        list_of_dictionaries = []
        for row in  csv.reader(io_string, delimiter=',', quotechar='|'):
            if row_count < 1:
                self.header_labels =  row
            else:
                row_dictionary = {}
                column_index = 0
                for column in row:
                    row_dictionary[self.header_labels[column_index]] = column
                    column_index +=1
                list_of_dictionaries.append(row_dictionary)
            row_count += 1
            self.data = list_of_dictionaries

    def search(self, search_string):
        results = []
        for obj in self.data:
            for key in obj:
                if search_string in obj[key]:
                    results.append(obj)
        return results

    def castInt(self, column):
        for obj in self.data:
            obj[column] = int(obj[column])

    def castFloat(self, column):
        for obj in self.data:
            obj[column] = float(obj[column])

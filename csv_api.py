import csv


class CSVConverter:
    def __init__(self, csv_path):
        self.csv_path = csv_path


    def open_csv(self):
        with open(self.csv_path, "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            return csv_reader


if __name__ == "__main__":
    obj = CSVConverter("prout.csv")
    print(type(obj.open_csv()))
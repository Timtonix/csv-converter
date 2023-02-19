import csv


class CSVConverter:
    def __init__(self, csv_path):
        self.csv_path = csv_path

    def open_csv(self):
        with open(self.csv_path, "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            csv_list = []
            for row in csv_reader:
                csv_list.append(row)

            return csv_list

    def get_csv_headers(self):
        csv = self.open_csv()
        return csv[0]


if __name__ == "__main__":
    obj = CSVConverter("prout.csv")
    print(type(obj.open_csv()))
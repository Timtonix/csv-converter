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
        csv_file = self.open_csv()
        return csv_file[0]

    def get_headers_position(self, headers: list) -> dict:
        csv_headers = self.get_csv_headers()
        headers_dict = {}

        for header in headers:
            if header in csv_headers:
                headers_dict[header] = csv_headers.index(header)
        return headers_dict

if __name__ == "__main__":
    obj = CSVConverter("prout.csv")
    obj.get_headers_position(["username", "password", "url"])
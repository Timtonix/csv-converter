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
            else:
                raise f"The header {header} is not in {headers}, please give existing headers !"
        return headers_dict

    def create_new_csv_list(self, headers: list) -> list:
        csv_file = self.open_csv()
        header_position = self.get_headers_position(headers)

        csv_list = []
        for line in csv_file:
            data_list = []
            for header in headers:
                if line[header_position[header]] == '':
                    line[header_position[header]] = "no_data"
                data_list.append(line[header_position[header]])
            csv_list.append(data_list)

        return csv_list

    def write_new_csv(self, headers: list):
        with open("updated_csv.csv", "w", newline="", encoding="UTF-8") as csv_write:
            writer = csv.writer(csv_write)
            writer.writerows(self.create_new_csv_list(headers))
        return "updated_csv.csv"





if __name__ == "__main__":
    obj = CSVConverter("prout.csv", ["username", "password", "url"])
    obj.get_headers_position()
    obj.write_new_csv()
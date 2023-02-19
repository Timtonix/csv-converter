import _csv
import csv
import csv_api


def test_open_csv(tmp_csv_file):
    with open(tmp_csv_file) as csv_file:
        csv_obj = csv_api.CSVConverter(tmp_csv_file)
        csv_opened = csv_obj.open_csv()
        assert type(csv_opened) == _csv.Reader

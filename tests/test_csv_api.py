import _csv
import csv
import csv_api


def test_open_csv(tmp_csv_file):
    with open(tmp_csv_file) as csv_file:
        csv_obj = csv_api.CSVConverter(tmp_csv_file)
        csv_opened = csv_obj.open_csv()
        assert type(csv_opened) == list


def test_get_headers(tmp_csv_file):
    csv_obj = csv_api.CSVConverter(tmp_csv_file)
    csv_headers = csv_obj.get_csv_headers()
    expected_headers = csv_obj.open_csv()[0]
    assert csv_headers == expected_headers

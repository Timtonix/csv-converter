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


def test_get_header_position(tmp_csv_file):
    csv_obj = csv_api.CSVConverter(tmp_csv_file)
    csv_headers_position = csv_obj.get_headers_position(["username", "url", "password"])
    expected_position = {"username": 1, "url": 0, "password": 2}
    assert csv_headers_position == expected_position


def test_create_new_csv(tmp_csv_file):
    pass

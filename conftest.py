import pytest
import csv_api


@pytest.fixture(scope="session")
def tmp_csv_file(tmp_path_factory):
    with open("/home/timtonix/Documents/PycharmProjects/csv-converter/tests/test_firefox.csv") as csv_file:
        path = tmp_path_factory.mktemp("csv") / "temp_csv.csv"
        path.write_text(csv_file.read())
        return path



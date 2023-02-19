import pytest



@pytest.fixture()
def csv_file():
    with open("tests/test.csv") as csv_file:
        return csv_file


@pytest.fixture()
def csv_data_list():
    return [["url", "username", "password"], ["https://jemangeduriz.com", "canard", "C01nCO1N"], ["https://youtube.com", "tintin", "C4ptA1neHadocqueu"]]


@pytest.fixture(scope="session")
def csv_object(tmp_path_factory, csv_file):
    csv_temp_path = tmp_path_factory.mktemp("csv")
    with open(f"{csv_temp_path}/temp_csv.csv", "w") as temp_csv_file:
        csv = temp_csv_file.write(csv_file)
        print(csv)
        yield csv
        temp_csv_file.close()

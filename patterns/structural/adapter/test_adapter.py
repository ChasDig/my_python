import json

from patterns.structural.adapter import CSVReader, Printer, JSONReader, JSON_DATA, CSV_DATA


def test_json_printer():
    json_reader = JSONReader()
    printer = Printer(reader=json_reader)
    result_ = json.loads(JSON_DATA)["items"]

    for num_, value in enumerate(printer.data_for_print(), start=0):
        assert result_[num_] == value


def test_csv_printer():
    csv_reader = CSVReader()
    printer = Printer(reader=csv_reader)

    lines = CSV_DATA.split("\n")
    headers, data_lst = lines[0].split(";"), lines[1:]
    result_ = [dict(zip(headers, data.split(";"))) for data in data_lst]

    for num_, value in enumerate(printer.data_for_print(), start=0):
        assert result_[num_] == value

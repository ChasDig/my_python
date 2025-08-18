import json
from typing import List

from patterns.structural.adapter import CSV_DATA, JSON_DATA
from .facade import ReadFacade


def test_facade():
    read_facade = ReadFacade()
    read_facade.json_data = JSON_DATA
    read_facade.csv_data = CSV_DATA

    result_json: List[dict] = json.loads(JSON_DATA)["items"]

    lines = CSV_DATA.split("\n")
    headers, data_lst = lines[0].split(";"), lines[1:]
    result_csv: List[dict] = [dict(zip(headers, data.split(";"))) for data in data_lst]

    for num_, value in enumerate(read_facade.get_json_data_for_print(), start=0):
        assert result_json[num_] == value

    for num_, value in enumerate(read_facade.get_csv_data_for_print(), start=0):
        assert result_csv[num_] == value

    result_all = [*result_json, *result_csv]
    for num_, value in enumerate(read_facade.get_all_data_for_print(), start=0):
        assert result_all[num_] == value
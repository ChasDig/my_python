import json
from typing import List, Generator
from abc import ABC, abstractmethod

CSV_DATA = "name;age\nDin;30\nSam;28"
JSON_DATA = (
    '{"items": [{"name": "Link", "age": "20"}, '
    '{"name": "Zelda", "age": "19"}]}'
)


class ReadAdapter(ABC):

    @abstractmethod
    def read_(self)-> List[dict]:
        pass


class CSVReader(ReadAdapter):

    def read_(self) -> List[dict]:
        headers, data_lst = self._get_csv_format_data()
        read_data = self._format_data_to_dict(headers=headers, data_lst=data_lst)

        return read_data

    def _get_csv_format_data(self) -> tuple:
        lines = self._get_lines()
        headers = lines[0].split(";")
        data_lst = (line.split(";") for line in lines[1:])

        return headers, data_lst

    @staticmethod
    def _get_lines() -> List[str]:
        return CSV_DATA.split("\n")

    @staticmethod
    def _format_data_to_dict(headers: list, data_lst: list) -> List[dict]:
        return [dict(zip(headers, data)) for data in data_lst]


class JSONReader(ReadAdapter):

    def read_(self) -> List[dict]:
        return json.loads(JSON_DATA)["items"]


class Printer:

    def __init__(self, reader: ReadAdapter) -> None:
        self._reader = reader

    def data_for_print(self) -> Generator[dict, None, None]:
        for item in self._reader.read_():
            yield item

import itertools
from typing import Generator

from patterns.adapter import JSONReader, CSVReader, Printer


class ReadFacade:

    def __init__(self) -> None:
        self._json_printer = Printer(reader=JSONReader())
        self._csv_printer = Printer(reader=CSVReader())
        self._json_data = list()
        self._csv_data = list()

    @property
    def json_data(self) -> list:
        return self._json_data

    @json_data.setter
    def json_data(self, data: list) -> None:
        self._json_data = data

    @property
    def csv_data(self) -> list:
        return self._csv_data

    @csv_data.setter
    def csv_data(self, data: list) -> None:
        self._csv_data = data

    def get_json_data_for_print(self) -> Generator[dict, None, None]:
        for data in self._json_printer.data_for_print():
            yield data

    def get_csv_data_for_print(self) -> Generator[dict, None, None]:
        for data in self._csv_printer.data_for_print():
            yield data

    def get_all_data_for_print(self) -> Generator[dict, None, None]:
        for data in itertools.chain(self.get_json_data_for_print(), self.get_csv_data_for_print()):
            yield data



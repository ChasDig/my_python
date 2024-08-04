import json
from abc import ABC, abstractmethod

########################################################################################################################
#
# https://refactoring.guru/ru/design-patterns/adapter/python/example#example-0
#
# Адаптер - Структурный Паттерн. Позволяет изолировать определенную часть интерфейса и определять его работу в
# зависимости от выбранного характера применяемой логики.
# - Пример: Адаптер может реализовать разную логику подключения к БД в зависимости от типа БД.
# - Промежуточная прослойка, позволяющая избавиться от жесткой связки между элементами архитектуры проекта.
#
########################################################################################################################

csv_source = 'first_name;second_name;\nPiter;Pen'
json_source = (
    '{"data": [{"first_name": "Din", "second_name": "Winchester"}, {"first_name": "Sam", "second_name": "Winchester"}]}'
)


class Adapter(ABC):

    @abstractmethod
    def get_data(self, source: str) -> list:
        pass


class JSONAdapter(Adapter):

    def get_data(self, source: str) -> list[dict[str, str]]:
        return json.loads(source).get("data", [])


class CSVAdapter(Adapter):

    def get_data(self, source: str) -> list[dict[str, str]]:
        source_lines = self._get_lines(source=source)
        headers, data = self._get_headers_with_data(source_lines=source_lines)

        return self._format_data(headers=headers, data=data)

    @staticmethod
    def _get_lines(source: str) -> list[str]:
        return source.split("\n")

    @staticmethod
    def _get_headers_with_data(source_lines: list[str]) -> tuple[list[str], list[list[str]]]:
        return source_lines[0].split(";"), [line.split(";") for line in source_lines[1:]]

    @staticmethod
    def _format_data(headers: list[str], data: list[list[str]]) -> list[dict[str, str]]:
        result: list[dict[str, str]] = list()

        for item in data:
            result.append(dict(zip(headers, item)))

        return result


class Reader:

    def __init__(self, adapter: Adapter) -> None:
        self._adapter = adapter

    @property
    def adapter(self) -> Adapter:
        return self._adapter

    def get_data(self, source: str) -> list[dict[str, str]]:
        return self.adapter.get_data(source=source)

    def print_source(self, source: str) -> None:
        for item in self.get_data(source=source):
            print("{} - {}".format(item.get("first_name", "NotFound"), item.get("second_name", "NotFound")))


if __name__ == "__main__":
    printer_csv = Reader(adapter=CSVAdapter())
    printer_json = Reader(adapter=JSONAdapter())

    printer_csv.print_source(source=csv_source)
    printer_json.print_source(source=json_source)

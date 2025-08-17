"""
S - Single Responsibility: принцип единой ответственности.
"""

## Bad:
class BadUser:

    def __init__(self, name: str) -> None:
        self.name = name

    def send(self, message: str) -> None:
        pass


## Good:
class GoodUser:

    def __init__(self, name: str) -> None:
        self.name = name


class GoodSendEmail:

    def send(self, email: str, message: str) -> None:
        pass

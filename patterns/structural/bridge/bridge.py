from abc import ABC, abstractmethod


class Abstraction:

    def __init__(self, implementation: 'Implementation') -> None:
        self._implementation= implementation

    def base_operation(self) -> str:
        return f"Abstraction: Base operation {self._implementation.operation_implementation()}"


class Implementation(ABC):

    @abstractmethod
    def operation_implementation(self) -> str:
        pass


class PlayStation(Abstraction):

    def base_operation(self) -> str:
        return f"console gaming on {self._implementation.operation_implementation()}"


class Computer(Abstraction):

    def base_operation(self) -> str:
        return f"computer gaming on {self._implementation.operation_implementation()}"


class GamePad(Implementation):

    def operation_implementation(self) -> str:
        return "gamepad"


class KeyboardAndMouse(Implementation):

    def operation_implementation(self) -> str:
        return "keyboard and mouse"


if __name__ == "__main__":
    play_station_with_gamepad = PlayStation(implementation=GamePad())
    computer_with_gamepad = Computer(implementation=GamePad())
    computer_with_keyboard_and_mouse = Computer(implementation=KeyboardAndMouse())

    print(play_station_with_gamepad.base_operation())
    print(computer_with_gamepad.base_operation())
    print(computer_with_keyboard_and_mouse.base_operation())
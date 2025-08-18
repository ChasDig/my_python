from abc import ABC, abstractmethod


class Component(ABC):

    @abstractmethod
    def operation(self) -> str:
        pass


class Decorator(Component):

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> Component:
        return self._component

    def operation(self) -> str:
        return self.component.operation()


class BaseComponent(Component):

    def operation(self) -> str:
        return self.__class__.__name__


class DecoratorA(Decorator):

    def operation(self) -> str:
        return f"{self.__class__.__name__}: {self.component.operation()}"


class DecoratorB(Decorator):

    def operation(self) -> str:
        return f"{self.__class__.__name__}: {self.component.operation()}"

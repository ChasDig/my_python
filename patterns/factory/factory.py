from typing import Type
from abc import ABC, abstractmethod


class TransportFactory(ABC):

    @abstractmethod
    def get_transport_method(self, type_transport: str) -> Type['Transport']:
        pass


    def start_deliver(self, type_transport) -> str:
        transport = self.get_transport_method(type_transport=type_transport)
        result = transport().deliver()

        return result


class Transport(ABC):

    @abstractmethod
    def deliver(self) -> str:
        pass


class CarFactory(TransportFactory):

    def get_transport_method(self, type_transport):
        transport_methods = {
            "bus": BusCar,
            "sedan": SedanCar,
        }

        return transport_methods[type_transport]


class BusCar(Transport):

    def deliver(self) -> str:
        return f"{self.__class__.__name__} start deliver on ground very slowly"


class SedanCar(Transport):

    def deliver(self) -> str:
        return f"{self.__class__.__name__} start deliver on ground fastly"


class AirplaneFactory(TransportFactory):

    def get_transport_method(self, type_transport):
        transport_methods = {
            "airbus": AirBus,
        }

        return transport_methods[type_transport]


class AirBus(Transport):

    def deliver(self) -> str:
        return f"{self.__class__.__name__} start deliver people on air very fast"

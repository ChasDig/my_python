import pytest

from .factory import CarFactory, AirplaneFactory


def test_car_factory():
    car_factory = CarFactory()
    bus_transport = car_factory.get_transport_method("bus")
    sedan_transport = car_factory.get_transport_method("sedan")

    assert bus_transport().deliver() == "BusCar start deliver on ground very slowly"
    assert sedan_transport().deliver() == "SedanCar start deliver on ground fastly"

def test_error_car_factory():
    car_factory = CarFactory()

    with pytest.raises(KeyError):
        car_factory.get_transport_method(type_transport="tank")


def test_airplane_factory():
    airplane_factory = AirplaneFactory()
    airbus_transport = airplane_factory.get_transport_method("airbus")

    assert airbus_transport().deliver() == "AirBus start deliver people on air very fast"


def test_error_airplane_factory():
    airplane_factory = AirplaneFactory()

    with pytest.raises(KeyError):
        airplane_factory.get_transport_method(type_transport="jets")

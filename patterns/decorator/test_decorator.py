from patterns.decorator import BaseComponent, DecoratorA, DecoratorB


def test_decorator():
    base_component = BaseComponent()
    assert "BaseComponent" == base_component.operation()

    decorator_a = DecoratorA(component=base_component)
    assert "DecoratorA: BaseComponent" == decorator_a.operation()

    decorator_b = DecoratorB(component=decorator_a)
    assert "DecoratorB: DecoratorA: BaseComponent" == decorator_b.operation()

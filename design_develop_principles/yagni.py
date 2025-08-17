"""
YAGNI (Your Ain`t Gonna Need It) - не реализуй функционал,
который 'может понадобиться'.
"""

def bad_example_calculate_discount(
    price: float,
    discount: float = 0.5,
    discount_type: str = "seasonal",
    region: str = "EN",
) -> float:
    return price * discount


def good_example_calculate_discount(
    price: float,
    discount: float = 0.5,
) -> float:
    return price * discount

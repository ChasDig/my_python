"""
SLAP (Single Level of Abstraction Principle) - это принцип программирования,
который требует, чтобы методы/функции выполняли задачи одного уровня
абстракции.
"""


# Bad:
def process_order_bad():
    # Проверка заказа
    ...

    # Расчет стоимости
    ...

    # Применение скидки
    ...


# Good:
def process_order_good():
    # Проверка заказа в отдельной функции
    check_order()

    # Расчет стоимости в отдельной функции
    calc_order()

    # Применение скидки в отдельной функции
    apply_discounts()


def check_order():
    pass


def calc_order():
    pass


def apply_discounts():
    pass

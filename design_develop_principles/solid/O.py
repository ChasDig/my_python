"""
O - Open/Closed Principle: принцип открытости/закрытости.
Объект должен быть доступен для расширения, но закрыт для изменений.
"""


# Good:
class Shape:
    def area(self):
        raise NotImplementedError()

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r ** 2

class Square(Shape):
    def __init__(self, s):
        self.s = s

    def area(self):
        return self.s ** 2

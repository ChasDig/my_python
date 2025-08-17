"""
I - Interface Segregation Principle: принцип разделения интерфейса (клиент не
должен зависеть от не используемого им интерфейса).
"""

# Bad
class Worker:

    def work(self):
        pass

    def eat(self):
        pass


class BadRobot(Worker):

    def work(self) -> str:
        return f"{self.__class__.__name__} works!"

    def eat(self):
        raise Exception(f"{self.__class__.__name__} not eat!")


# Good:
class Workable:

    def work(self):
        pass


class Eatable:

    def eat(self):
        pass


class GoodRobot(Worker):

    def work(self) -> str:
        return f"{self.__class__.__name__} works!"


class Human:

    def work(self) -> str:
        return f"{self.__class__.__name__} not like works!"

    def eat(self):
        raise Exception(f"{self.__class__.__name__} like eat!")

"""
L - Liskov Substitution Principle: подклассы должны заменять объекты базовых
классов без нарушения работы программы (ковариантность).
"""


# Bad:
class BadAnimal:
    def say(self, what_say: str) -> str:
        return f"{self.__class__.__name__} say {what_say}"


class BadNotTalkingAnimal(BadAnimal):
    def say(self, what_say: str) -> str:
        raise NotImplementedError(
            f"{self.__class__.__name__} can`t say anything"
        )


# Good:
class GoodAnimal:
    pass


class GoodTalkingAnimal(GoodAnimal):
    def say(self, what_say: str) -> str:
        return f"{self.__class__.__name__} say {what_say}"


class GoodNotTalkingAnimal(GoodAnimal):
    pass

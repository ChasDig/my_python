"""
SOC (Separation of Concerns) - принцип разделения функционала по областям.
"""

class Base:

    def __init__(self, name: str) -> None:
        self.name = name


class User(Base):
    pass


class DB:

    @staticmethod
    def save(obj: Base) -> None:
        print(
            f"Obj '{obj.__class__.__name__}' with name '{obj.name}' was save"
        )


# Bad
def bad_create_and_save_user(user_name: str) -> None:
    user = User(name=user_name)
    DB.save(obj=user)


# Good
def good_create_user(user_name: str) -> User:
    return User(name=user_name)


def good_save_user(user: User) -> None:
    DB.save(obj=user)

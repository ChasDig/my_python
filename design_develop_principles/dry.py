"""
DRY (Don`t Repeat Yourself) - избегай дубли (не повторяй).
"""
from typing import Any


class User:

    def __init__(self, name: str, email: str, is_active: bool = True) -> None:
        self.name = name
        self.email = email
        self.is_active = is_active

    def bad_get_user_email(self) -> str | None:
        return self.email if self.is_active is True else None

    def bad_get_user_name(self) -> str | None:
        return self.name if self.is_active is True else None

    def good_get_user_attr(self, attr: str) -> Any:
        return getattr(self, attr) if self.is_active else None

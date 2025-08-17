"""
D - Dependency Inversion Principle: принцип инверсии зависимостей (зависимость
должна идти от абстракций, а не от конкретных реализаций).
"""

# Good:
class MessageSender:

    def send(self, message: str, to_: str) -> None:
        raise NotImplementedError()


class EmailSender(MessageSender):

    def send(self, message: str, to_: str) -> None:
        print(f"Email send to {to_}")


class Notifier:

    def __init__(self, sender: MessageSender) -> None:
        self.sender = sender

    def notify(self, message: str, to_: str) -> None:
        self.sender.send(message=message, to_=to_)

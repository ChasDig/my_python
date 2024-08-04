from abc import ABC, abstractmethod
from random import choice
from typing import Optional


########################################################################################################################
# #
# https://refactoring.guru/ru/design-patterns/observer
#
# Наблюдатель — это поведенческий паттерн проектирования, который создаёт механизм подписки, позволяющий одним
# объектам следить и реагировать на события, происходящие в других объектах.
#
########################################################################################################################


class Publisher(ABC):
    """Class-Publisher for control Subscribers."""

    state_: Optional[str] = None  # State publisher: [inactive, active]
    subscribers_: list['Subscriber'] = list()

    @abstractmethod
    def attach(self, subscriber: 'Subscriber') -> None:
        """Append a subscriber to the publisher."""
        pass

    @abstractmethod
    def detach(self, subscriber: 'Subscriber') -> None:
        """Detach asubscriber from a publisher."""
        pass

    @abstractmethod
    def notify(self) -> None:
        """Notify subscribers."""
        pass


class SimplePublisher(Publisher):

    def attach(self, subscriber: 'Subscriber') -> None:
        self.subscribers_.append(subscriber)

        print("Subject: attached subscriber")

    def detach(self, subscriber: 'Subscriber') -> None:
        self.subscribers_.remove(subscriber)

        print("Subject: detach subscriber")

    def notify(self) -> None:
        for subscriber in self.subscribers_:
            subscriber.update(self)

        print("Subscribers was notified")

    def execute_some_logic(self) -> None:

        publisher_state = choice(("active", "inactive"))
        self.state_ = publisher_state

        self.notify()


class Subscriber(ABC):
    """Class-Subscriber."""

    @abstractmethod
    def update(self, publisher: Publisher) -> None:
        """Update stated Subscriber"""
        pass


class SubscriberOnActivePublisher(Subscriber):

    def update(self, publisher: Publisher) -> None:

        if publisher.state_ == "active":
            print("Was notified subscriber on active publisher")


class SubscriberOnInactivePublisher(Subscriber):

    def update(self, publisher: Publisher) -> None:

        if publisher.state_ == "inactive":
            print("Was notified subscriber on inactive publisher")


if __name__ == "__main__":
    simple_publisher = SimplePublisher()

    subscriber_on_active_publisher = SubscriberOnActivePublisher()
    simple_publisher.attach(subscriber=subscriber_on_active_publisher)

    subscriber_on_inactive_publisher = SubscriberOnInactivePublisher()
    simple_publisher.attach(subscriber=subscriber_on_inactive_publisher)

    simple_publisher.execute_some_logic()
    simple_publisher.execute_some_logic()

    simple_publisher.detach(subscriber=subscriber_on_active_publisher)
    simple_publisher.detach(subscriber=subscriber_on_inactive_publisher)

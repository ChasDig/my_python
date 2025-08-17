from threading import Lock


class SingletonMeta(type):
    """Реализация паттерна Singleton в 'однопоточной' среде."""

    _instances = dict()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances.keys():
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance

        return cls._instances[cls]


class Session(metaclass=SingletonMeta):
    pass


class SingletonThreadMeta(type):
    """Реализация паттерна Singleton в 'многопоточной' среде."""

    _instances = dict()
    _locker = Lock()

    def __call__(cls, *args, **kwargs):
        """
        При первом вызове потомка, _locker будет блокировать для других
        потоков доступ к вызову, пока не выполниться весь код в методе. После
        снятия блокировки повторные запросы не будут проходить по условию.

        :param args:
        :param kwargs:
        :return:
        """
        with cls._locker:
            if cls not in cls._instances.keys():
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance

        return cls._instances[cls]


class SessionThread(metaclass=SingletonThreadMeta):
    pass

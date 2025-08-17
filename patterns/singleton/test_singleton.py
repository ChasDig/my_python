from threading import Thread

from .singleton import Session, SessionThread


def test_singleton():
    session_1 = Session()
    session_2 = Session()

    assert id(session_1) == id(session_2)


def add_obj_in_lst(lst: list):
    lst.append(SessionThread())


def test_singleton_thread():
    instances = list()

    process_1 = Thread(target=add_obj_in_lst, args=(instances,))
    process_2 = Thread(target=add_obj_in_lst, args=(instances,))

    process_1.start()
    process_2.start()
    process_1.join()
    process_2.join()

    assert len(instances) == 2
    assert id(instances[0]) == id(instances[1])


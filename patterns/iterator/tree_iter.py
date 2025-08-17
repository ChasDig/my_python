def tree(class_):
    yield class_.__name__, 0
    yield from subtree(class_, lvl=1)


def subtree(class_, lvl):
    for subclass in class_.__subclasses__():
        yield subclass.__name__, lvl
        yield from subtree(subclass, lvl=lvl + 1)


def display(class_):
    for class_name, lvl in tree(class_):
        print("\t" * lvl, class_name)


# ---- #
import typing


def average(max_ = 5) -> typing.Generator[float, float, tuple[float, int]]:
    total = 0.0
    count = 0
    average_ = 0.0

    while True:
        term = yield average_

        if count == max_:
            break

        total += term
        count += 1
        average_ = total / count

    return average_, count

if __name__ == "__main__":
    display(BaseException)

    lst = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
    coro_aver = average(max_=len(lst) - 1)
    print(next(coro_aver))
    try:
        for i in lst:
            print(coro_aver.send(i))

    except StopIteration as ex:
        print(ex)


import re
from collections.abc import Iterable, Iterator
from typing import Any


class CollectionIterator(Iterator):

    def __init__(self, collection: 'WordsCollectionIterable') -> None:
        self._collection = collection
        self._position = 0

    def __next__(self) -> Any:
        try:
            value = self._collection[self._position]
            self._position += 1

        except IndexError:
            raise StopIteration()

        return value

    def __iter__(self):
        return self


class WordsCollectionIterable(Iterable):

    def __init__(self, collection: list) -> None:
        self._collection = collection

    def __getitem__(self, item) -> Any:
        return self._collection[item]

    def __iter__(self):
        return CollectionIterator(self)


class LazyTextGen:
    RE_WORD = re.compile(r"\w+")

    def __init__(self, text: str):
        self._text = text

    def __iter__(self):
        return (match.group() for match in self.RE_WORD.finditer(self._text))


class ArithmeticProcession:

    def __init__(self, start, step, stop = None):
        self._start = start
        self._step = step
        self._stop = stop

    def __iter__(self):
        is_forever = True if self._stop is None else False
        type_ = type(self._start + self._step)
        result = type_(self._start)

        # index = 0
        while is_forever or result < self._stop:
            yield result

            result += self._step
            # index += 1
            # result = self._start + self._step * index

import itertools


def arithmetic_gen(start, step, stop = None):
    first = type(start + step)(start)
    gen_ap = itertools.count(first, step)

    if stop:
        return itertools.takewhile(lambda x: x < stop, gen_ap)

    return gen_ap
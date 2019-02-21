from typing import TypeVar, Iterable, Any
from linkedlist import SingleNode

T = TypeVar('T')


class Bag:
    def __init__(self):
        super(Bag, self).__init__()
        self._first = None
        self._size = 0

    def add(self, val: T) -> None:
        self._first = SingleNode(val, self._first)
        self._size += 1

    def empty(self) -> bool:
        return self._size == 0

    def clear(self) -> None:
        self._first = None
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def __iter__(self):
        self._cur = self._first
        return self

    def __next__(self) -> T:
        if self._cur is None:
            raise StopIteration
        val = self._cur.value
        self._cur = self._cur.next
        return val

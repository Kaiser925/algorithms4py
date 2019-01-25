from typing import Optional, Iterable
from linkedlist import SingleNode


class Bag(object):
    def __init__(self):
        super(Bag, self).__init__()
        self._first = None
        self._size = 0

    def add(self, val: Optional) -> None:
        self._first = SingleNode(val, self._first)
        self._size += 1

    def empty(self) -> bool:
        return self._size == 0

    def clear(self):
        self._first = None
        self._size = 0

    def __len__(self):
        return self._size

    def __iter__(self) -> Iterable:
        self._cur = self._first
        return self

    def __next__(self) -> Optional:
        if self._cur is None:
            raise StopIteration
        val = self._cur.value
        self._cur = self._cur.next
        return val

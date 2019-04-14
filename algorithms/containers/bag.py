from typing import TypeVar, Iterable, Any
from linkedlist import SingleNode, ContainerIterMixin

T = TypeVar('T')


class Bag(ContainerIterMixin):
    def __init__(self):
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

from typing import Optional, Iterable, TypeVar
from linkedlist import SingleNode, ContainerIterMixin

T = TypeVar("T")


class Stack(ContainerIterMixin):
    def __init__(self):
        self._first = None
        self._size = 0

    def clear(self) -> None:
        self._first = None
        self._size = 0

    def push(self, val: T) -> None:
        """push the element to stack.
        """
        node = SingleNode(val, self._first)
        self._first = node
        self._size += 1

    def pop(self) -> Optional[T]:
        """Pop the top element from stack.

        If stack is empty, it will return None,
        else return the value of top element.
        """
        if self._size == 0:
            return None
        item = self._first
        self._first = self._first.next
        self._size -= 1
        return item.value

    def empty(self) -> bool:
        return self._size == 0

    def peek(self) -> Optional[T]:
        """Peek return the value of top element without removing it.

        If stack is empty, it will return None.
        """
        if self._first is None:
            return None
        else:
            return self._first.value

    def __len__(self) -> int:
        return self._size

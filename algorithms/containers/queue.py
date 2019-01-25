from typing import Optional, Iterable
from linkedlist import SingleNode


class Queue(object):
    def __init__(self):
        super(Queue, self).__init__()
        self._first = None
        self._last = None
        self._len = 0

    def clear(self) -> None:
        self._first = None
        self._last = None
        self._len = 0

    def enqueue(self, val: Optional) -> None:
        old_last = self._last
        self._last = SingleNode(val, None)
        if self.empty():
            self._first = self._last
        else:
            old_last.next = self._last
        self._len += 1

    def peek(self):
        if self._first is None:
            return None
        else:
            return self._first.value

    def dequeue(self) -> Optional:
        if self.empty():
            self._last = None
            return None
        val = self._first.value
        self._first = self._first.next
        self._len -= 1
        return val

    def empty(self) -> bool:
        return self._len == 0

    def __len__(self):
        return self._len

    def __iter__(self) -> Iterable:
        self._cur = self._first
        return self

    def __next__(self) -> Optional:
        if self._cur is None:
            raise StopIteration
        val = self._cur.value
        self._cur = self._cur.next
        return val

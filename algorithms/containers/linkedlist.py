from __future__ import annotations
from typing import TypeVar, Optional

T = TypeVar("T")

class ContainerIterMixin(object):
    def __iter__(self):
        self._cur = self._first
        return self

    def __next__(self):
        if self._cur is None:
            raise StopIteration
        else:
            elem = self._cur
            self._cur = self._cur.next
            return elem.value


class SingleNode(object):
    def __init__(self, value: T, next_node: Optional[SingleNode]) -> None:
        self.value = value
        self.next = next_node


class DoublyNode(object):
    def __init__(self, value: T) -> None:
        self.value = value
        self.prev = None # type: Optional[DoublyNode]
        self.next = None # type: Optional[DoublyNode]


class DoublyLinkedList(ContainerIterMixin):
    def __init__(self):
        self._first = None # type: Optional[DoublyNode]
        self._last = None # type: Optional[DoublyNode]
        self._len: int = 0

    def add(self, value: T) -> None:
        node = DoublyNode(value)
        node.prev = self._last
        if self._len == 0:
            self._first = node
            self._last = node
        else:
            if self._last is None:
                raise ValueError("_last is none.")
            self._last.next = node
            self._last = node
        self._len += 1

    def get(self, index: int) -> T:
        if index >= self._len or index < 0:
            raise IndexError("DoublyLinkedList index out of range")

        elem = self._first  # type: Optional[DoublyNode]

        for i in range(self._len):
            if elem is None:
                raise ValueError("Has none node in list.")
            if i == index:
                value = elem.value
                break
            elem = elem.next
        return value

    def remove(self, index: int) -> None:
        if index >= self._len or index < 0:
            raise IndexError("DoublyLinkedList index out of range")

        if self._len == 1:
            self.clear()
            return

        elem = self._first  # type: Optional[DoublyNode]
        for i in range(self._len):
            if elem is None:
                raise ValueError("Has none node in list.")
            if i == index:
                break
            elem = elem.next

        if elem == self._first:
            self._first =  elem.next if elem else None
        if elem == self._last:
            self._last = elem.prev if elem else None

        if elem and elem.prev:
            elem.prev.next = elem.next

        if elem and elem.next:
            elem.next.prev = elem.prev

        elem = None
        self._len -= 1

    def indexOf(self, value: T) -> int:
        if self._len == 0:
            return -1
        cur = self._first  # type: Optional[DoublyNode]
        for i in range(self._len):
            if cur and cur.value == value:
                return i
            cur = cur.next if cur else None
        return -1

    def insert(self, index: int, value: T) -> None:
        if index >= self._len or index < 0:
            raise IndexError("DoublyLinkedList index out of range")
        cur = self._first # type: Optional[DoublyNode]

        for i in range(self._len):
            if i == index:
                break
            cur = cur.next if cur else None

        if cur == self._first:
            old = self._first
            new = DoublyNode(value)
            new.prev = None
            new.next = old
            if old is None:
                raise ValueError("_first is None.")
            old.prev = new
            self._first = new
        else:
            old = cur
            new = DoublyNode(value)
            new.prev = old.prev if old else None
            new.next = old
            if old and old.prev:
                old.prev.next = new
                old.prev = new
        llist._len += 1

    def clear(self):
        self._len = 0
        self._first = None
        self._last = None

    def __len__(self):
        return self._len

    # def __iter__(self):
    #     self._cur = self._first
    #     return self

    # def __next__(self):
    #     if self._cur is None:
    #         raise StopIteration
    #     else:
    #         elem = self._cur
    #         self._cur = self._cur.next
    #         return elem.value


if __name__ == '__main__':
    llist = DoublyLinkedList()

    for x in range(11):
        llist.add(x)

    llist.remove(10)
    llist.remove(0)
    llist.remove(5)
    passed = True

    if len(llist) != 8:
        print(f"Len error: excepted {8}, got {len(llist)}")
        passed = False

    if llist.indexOf(1) != 0:
        print(f"indexOf() error: excepted {0}, got{llist.indexOf(1)}")
        passed = False

    llist.clear()
    if len(llist) != 0:
        print(f"Len error: excepted {0}, got {len(llist)}")
        passed = False

    llist.add(3)
    llist.insert(0, -1)
    llist.insert(1, 1)
    llist.insert(2, 2)

    for i in iter(llist):
        print(i)

    if passed:
        print("pass")

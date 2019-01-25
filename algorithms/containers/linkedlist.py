from typing import Optional


class SingleNode(object):
    def __init__(self, value: Optional, next_node: Optional) -> None:
        self.value = value
        self.next = next_node


class DoubleNode(object):
    def __init__(self, value: Optional, prev_node: Optional,
                 next_node: Optional) -> None:
        self.value = value
        self.prev = prev_node
        self.next = next_node


class DoublyLinkedList(object):
    def __init__(self):
        self._first: DoubleNode = None
        self._last: DoubleNode = None
        self._len: int = 0

    def add(self, value: Optional) -> None:
        node = DoubleNode(value, self._last, None)
        if self._len == 0:
            self._first = node
            self._last = node
        else:
            self._last.next = node
            self._last = node
        self._len += 1

    def get(self, index: int) -> Optional:
        if index >= self._len or index < 0:
            raise IndexError("DoublyLinkedList index out of range")

        elem = self._first
        for i in range(self._len):
            if i == index:
                return elem.value
            elem = elem.next

    def remove(self, index: int) -> None:
        if index >= self._len or index < 0:
            raise IndexError("DoublyLinkedList index out of range")

        if self._len == 1:
            self.clear()
            return

        elem = self._first
        for i in range(self._len):
            if i == index:
                break
            elem = elem.next

        if elem == self._first:
            self._first = elem.next
        if elem == self._last:
            self._last = elem.prev

        if elem.prev is not None:
            elem.prev.next = elem.next

        if elem.next is not None:
            elem.next.prev = elem.prev

        elem = None
        self._len -= 1

    def indexOf(self, value: Optional) -> int:
        if self._len == 0:
            return -1
        cur = self._first
        for i in range(self._len):
            if cur.value == value:
                return i
            cur = cur.next
        return -1

    def insert(self, index: int, value: Optional) -> None:
        if index >= self._len or index < 0:
            raise IndexError("DoublyLinkedList index out of range")
        cur = self._first

        for i in range(self._len):
            if i == index:
                break
            cur = cur.next

        if cur == self._first:
            old = self._first
            new = DoubleNode(value, None, old)
            old.prev = new
            self._first = new
        else:
            old = cur
            new = DoubleNode(value, old.prev, old)
            old.prev.next = new
            old.prev = new

        llist._len += 1

    def clear(self):
        self._len = 0
        self._first = None
        self._last = None

    def __len__(self):
        return self._len

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

#coding: utf-8

class Node(object):
    def __init__(self, elem, _next=None):
        self.elem = elem
        self._next = _next


class SingleLinkedList(object):
    def __init__(self):
        self.head = None

    @property
    def is_empty(self):
        return self.head == None

    def add(self, elem):
        node = Node(elem)
        if self.is_empty:
            self.head = node
        else:
            current = self.head
            self.head = node
            node._next = current

    def pop(self):
        if self.is_empty:
            raise ValueError('SingleLinkedList is empty')
        _next = self.head._next
        self.head = _next

    def traverse(self):
        if self.is_empty:
            raise ValueError('SingleLinkedList is empty')
        current = self.head
        while current:
            print current.elem
            current = current._next

    def remove(self, elem):
        if self.is_empty:
            raise ValueError('SingleLinkedList is empty')
        else:
            if self.head.elem == elem:
                self.head = self.head._next
            else:
                current = self.head._next
                prev = self.head
                while current:
                    if current.elem == elem:
                        prev._next = current._next
                        return
                    prev = current
                    current = current._next

    # 逆转链表
    def reverse(self):
        if self.is_empty:
            raise ValueError('SingleLinkedList is empty')
        current = self.head
        prev = None
        while current:
            _next = current._next
            current._next = prev
            prev = current
            current = _next
        self.head = prev

    # 链表节点成对交换
    def swap_pairs(self):
        if self.is_empty:
            raise ValueError('SingleLinkedList is empty')
        current = self.head
        prev = None
        while current._next:
            _next = current._next
            current._next = _next._next
            _next._next = current

            if prev:
                prev._next = _next
            else:
                self.head = _next

            if current._next:
                prev = current
                current = current._next
            else:
                break



l = SingleLinkedList()
l.add(1)
l.add(2)
l.add(3)
l.add(4)
# l.pop()
l.traverse()
print ''
l.reverse()
# l.swap_pairs()
l.traverse()
print ''
l.remove(3)
l.traverse()

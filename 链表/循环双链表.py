#coding: utf-8
"""
循环双链表只要存在首结点或尾节点，都能实现时间复杂度O(1)首尾两端
的元素插入/删除操作
"""
from exceptions import ValueError

class UnderFlow(ValueError):
    pass

class LNode(object):

    def __init__(self, elem, prev=None, _next=None):
        self.elem = elem
        self.prev = prev
        self._next = _next

class CircleDoubleLList(object):

    def __init__(self):
        self.head = None

    def prepend(self, elem):
        n = LNode(elem)
        if self.head == None:
            self.head = n
            n._next = n
            n.prev = n
        else:
            n._next = self.head
            n.prev = self.head.prev
            self.head.prev._next = n
            self.head.prev = n

    def append(self, elem):
        n = LNode(elem)
        if self.head == None:
            self.head = n
            n._next = n
            n.prev = n
        else:
            self.head.prev._next = n
            n.prev = self.head.prev
            n._next = self.head
            self.head.prev = n

    def traverse(self):
        current = self.head
        while True:
            print current.elem
            if current == self.head.prev:
                break
            current = current._next

    def prepop(self):
        if self.head == None:
            raise UnderFlow('LList is empty')

        elem = self.head.elem
        if self.head._next == self.head:
            self.head = None
            return elem
        else:
            self.head.prev._next = self.head._next
            self.head._next.prev = self.head.prev
            self.head = self.head._next
            return elem

    def pop(self):
        if self.head == None:
            raise UnderFlow('LList is empty')

        if self.head._next == self.head:
            elem = self.head.elem
            self.head = None
            return elem
        else:
            elem = self.head.prev.elem
            self.head.prev = self.head.prev.prev
            self.head.prev._next = self.head
            return elem

c = CircleDoubleLList()
c.prepend(1)
c.prepend(2)
c.prepend(3)
c.prepend(4)
c.append(5)
c.append(6)
c.append(7)
c.append(8)
c.traverse()
print ''
c.pop()
c.traverse()
from exceptions import ValueError

class OverFlow(ValueError):
    pass

class LNode(object):

    def __init__(self, elem, prev=None, _next=None):
        self.elem = elem
        self.prev = prev
        self._next = _next


class DoubleLList(object):

    def __init__(self):
        self.head = None
        self.rear = None

    def is_empty(self):
        return self.head == None

    def prepend(self, elem):
        n = LNode(elem)
        if self.is_empty():
            self.rear = n
        else:
            n._next = self.head
            self.head.prev = n
        self.head = n

    def append(self, elem):
        n = LNode(elem)
        if self.is_empty():
            self.head = n
        else:
            self.rear._next = n
            n.prev = self.rear
        self.rear = n

    def prepop(self):
        if self.is_empty():
            raise OverFlow('LList is empty')

        elem = self.head.elem
        if self.head._next == None:
            self.head = None
            self.rear = None
            return elem
        else:
            self.head = self.head._next
            self.head.prev = None
            return elem

    def pop(self):
        if self.is_empty():
            raise OverFlow('LList is empty')

        elem = self.head.elem
        if self.head._next == None:
            self.head = None
            self.rear = None
            return elem
        else:
            self.rear = self.rear.prev
            self.rear._next.prev = None
            self.rear._next = None
            return elem

    def traverse(self):
        current = self.head
        while current != None:
            print current.elem
            current = current._next


d = DoubleLList()
# d.prepend(1)
# d.prepend(2)
# d.prepend(3)
# d.prepend(4)
# d.append(5)
# d.append(6)
d.append(7)
d.append(8)
d.traverse()
print ''
d.pop()
d.traverse()




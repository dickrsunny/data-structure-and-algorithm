from exceptions import ValueError

class UnderFlow(ValueError):
    pass

class LNode(object):
    def __init__(self, elem, _next=None):
        self.elem = elem
        self._next = None

class CircleLList(object):

    def __init__(self):
        self.rear = None

    def is_empty(self):
        return self.rear == None

    def prepend(self, elem):
        n = LNode(elem)
        if self.rear == None:
            n._next = n
            self.rear = n
        else:
            n._next = self.rear._next
            self.rear._next = n

    def append(self, elem):
        self.prepend(elem)
        self.rear = self.rear._next

    def traverse(self):
        if self.is_empty():
            return
        current = self.rear._next
        while True:
            print current.elem
            if current == self.rear:
                break
            current = current._next

    def prepop(self):
        if self.rear == None:
            raise UnderFlow('LList Empty')
        if self.rear._next == self.rear:
            self.rear = None
        else:
            self.rear._next = self.rear._next._next

    def pop(self):
        if self.rear == None:
            raise UnderFlow('LList Empty')
        if self.rear._next == self.rear:
            self.rear = None
        else:
            current = self.rear._next
            while current._next != self.rear:
                current = current._next
            current._next = self.rear._next
            self.rear = current





c = CircleLList()
# c.prepend(1)
# c.prepend(2)
# c.prepend(3)
# c.prepend(4)
# c.append(5)
# c.append(6)
c.append(7)
c.append(8)
c.traverse()
print ''
c.pop()
# c.pop()
print ''
c.traverse()
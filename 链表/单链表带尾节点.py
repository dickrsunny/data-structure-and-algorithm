from exceptions import ValueError

class OverFlow(ValueError):
    pass

class LNode(object):
    def __init__(self, elem, _next=None):
        self.elem = elem
        self._next = None


class LListWithTailNode(object):

    def __init__(self):
        self.head = None
        self.rear = None

    def is_empty(self):
        return self.head == None

    def prepend(self, elem):
        n = LNode(elem)
        if self.is_empty():
            self.head = n
            self.rear = n
            return
        else:
            n._next = self.head
            self.head = n

    def append(self, elem):
        n = LNode(elem)
        if self.is_empty():
            self.head = n
            self.rear = n
        else:
            self.rear._next = n
            self.rear = n

    def prepop(self):
        if self.is_empty():
            raise OverFlow('LList is empty')
        current = self.head
        if current._next == None:
            elem = self.head.elem
            self.head = None
            self.rear = None
            return elem
        else:
            elem = self.head.elem
            self.head = self.head._next
            return elem

    def pop(self):
        if self.is_empty():
            raise OverFlow('LList is empty')
        current = self.head
        if current._next == None:
            elem = self.head.elem
            self.head = None
            self.rear = None
            return elem
        else:
            while current._next._next != None:
                current = current._next
            elem = current._next.elem
            current._next = None
            self.rear = current
            return elem

    def traverse(self):
        current = self.head
        while current != None:
            print current.elem
            current = current._next


l = LListWithTailNode()
l.prepend(1)
# l.prepend(2)
# l.prepend(3)
# l.prepend(4)
# l.traverse()
# print l.rear.elem, '\n'
# l.append(5)
# l.append(6)
l.traverse()
# print l.rear.elem
print l.pop(), '\n'





from exceptions import ValueError

class UnderFlow(ValueError):
    pass

class Node(object):

    def __init__(self, elem):
        self.elem = elem
        self.next_ = None

class LList(object):

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def prepend(self, elem):
        node = Node(elem)
        if self.is_empty():
            self.head = node
        else:
            node.next_ = self.head
            self.head = node

    def prepop(self):
        if self.is_empty():
            raise UnderFlow('LList is empty')

        if self.head.next_ == None:
            self.head = None
        else:
            self.head = self.head.next_

    def traverse(self):
        current = self.head
        while current != None:
            print current.elem
            current = current.next_

class Stack(object):

    l = LList()

    def is_empty(self):
        return self.l.is_empty()

    def top(self):
        if self.l.is_empty():
            raise UnderFlow('Stack is empty')
        return self.l.head

    def push(self, elem):
        self.l.prepend(elem)

    def pop(self):
        self.l.prepop()

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.l.traverse()
s.pop()
s.l.traverse()



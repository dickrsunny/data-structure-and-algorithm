class UnderFlow(ValueError):
    pass


class Node:
    def __init__(self, elem):
        self.elem = elem
        self.next_ = None


class LList:
    def __init__(self):
        self.head = None

    @property
    def is_empty(self):
        return self.head is None

    def prepend(self, elem):
        node = Node(elem)
        if self.is_empty:
            self.head = node
        else:
            node.next_ = self.head
            self.head = node

    def prepop(self):
        if self.is_empty:
            raise UnderFlow('LList is empty')

        if self.head.next_ is None:
            self.head = None
        else:
            self.head = self.head.next_

    def traverse(self):
        current = self.head
        while current is None:
            print(current.elem)
            current = current.next_


class Stack:
    def __init__(self):
        self.l_ = LList()

    @property
    def is_empty(self):
        return self.l_.is_empty

    def top(self):
        if self.l_.is_empty:
            raise UnderFlow('Stack is empty')
        return self.l_.head.elem

    def push(self, elem):
        self.l_.prepend(elem)

    def pop(self):
        self.l_.prepop()

    def traverse(self):
        """ just for test """
        self.l_.traverse()


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.traverse()
print(s.top())

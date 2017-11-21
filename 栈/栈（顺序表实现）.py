from exceptions import ValueError

class UnderFlow(ValueError):
    pass

class Stack(object):

    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def top(self):
        if self.is_empty():
            raise UnderFlow('Stack is empty')
        return self.elems[-1]

    def push(self, elem):
        self.elems.append(elem)

    def pop(self):
        if self.is_empty():
            raise UnderFlow('Stack is empty')
        self.elems.pop()

s = Stack()
s.push(1)
s.push(2)
print s.elems
s.pop()
s.pop()
print s.elems
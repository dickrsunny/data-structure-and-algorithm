from exceptions import Exception

class UnderFlow(Exception):
    pass

class Queue(object):

    def __init__(self, length=4):
        self.length = length
        self.elems = [0] * length
        self.head = 0
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def peek(self):
        if self.is_empty():
            raise UnderFlow()
        return self.elems[self.head]

    def dequeue(self):
        if self.is_empty():
            raise UnderFlow()
        elem = self.elems[self.head]
        self.head = (self.head + 1) % self.length
        self.count -= 1
        return elem

    def __expand(self):
        new_length = self.length * 2
        list_ = [0] * new_length
        for i in range(self.length):
            list_[i] = self.elems[(self.head + i) % self.length]
        self.elems = list_
        self.head = 0
        self.length = new_length

    def enqueue(self, elem):
        if self.count == self.length:
            self.__expand()
        self.elems[(self.head + self.count) % self.length] = elem
        self.count += 1


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.dequeue()
print q.elems
q.enqueue(5)
q.enqueue(6)
print q.elems



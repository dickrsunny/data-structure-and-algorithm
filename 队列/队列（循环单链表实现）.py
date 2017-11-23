# coding: utf-8

from exceptions import Exception


class UnderFlow(Exception):
    pass


class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next_ = None


class CircleSingleLList(object):
    def __init__(self):
        self.rear = None

    def is_empty(self):
        return self.rear == None

    def append(self, elem):
        node = Node(elem)
        if self.is_empty():
            node.next_ = node
            self.rear = node
        else:
            node.next_ = self.rear.next_
            self.rear.next_ = node
            self.rear = self.rear.next_

    def prepop(self):
        if self.is_empty():
            raise UnderFlow()

        if self.rear.next_ == self.rear:
            self.rear = None
        else:
            self.rear.next_ = self.rear.next_.next_

    def traverse(self):
        if self.is_empty():
            return

        current = self.rear.next_
        while True:
            print current.elem
            if current == self.rear:
                break
            current = current.next_


class Queue(object):

    def __init__(self):
        self.c = CircleSingleLList()

    def is_empty(self):
        return self.c.is_empty()

    def peek(self):
        if self.is_empty():
            raise UnderFlow()
        return self.c.rear.next_.elem

    def enqueue(self, elem):
        self.c.append(elem)

    def dequeue(self):
        self.c.prepop()

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.c.traverse()
print ''
print q.peek()
print ''
q.dequeue()
q.dequeue()
q.c.traverse()
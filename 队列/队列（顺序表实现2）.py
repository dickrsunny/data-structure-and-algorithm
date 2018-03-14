class Queue:
    def __init__(self):
        self.elems = [None] * 4
        self.head = 0
        self.count = 0
        self.rear = 0

    @property
    def is_empty(self):
        return self.count == 0

    @property
    def length(self):
        return len(self.elems)

    def __extend(self):
        _list = [None] * self.length * 2
        i = 0
        for j in self.elems[self.head:]:
            _list[i] = j
            i += 1
        for k in self.elems[:self.head]:
            _list[i] = k
            i += 1
        self.elems = _list
        self.head = 0
        self.rear = i

    def enqueue(self, elem):
        if self.count == self.length:
            self.__extend()
        self.elems[self.rear] = elem

        self.rear = (self.rear + 1) % self.length
        self.count += 1

    def __shrink(self):
        _list = [None] * (self.length // 2)
        i = 0
        j = self.head
        while j < self.length and self.elems[j]:
            _list[i] = self.elems[j]
            i += 1
            j += 1
        if self.rear < self.head:
            k = 0
            while k < self.rear:
                _list[i] = self.elems[k]
                i += 1
                k += 1
        self.elems = _list
        self.head = 0
        self.rear = i

    def dequeue(self):
        if self.is_empty:
            raise ValueError('Queue is empty')
        elem = self.elems[self.head]
        self.elems[self.head] = None
        self.head = (self.head + 1) % self.length
        self.count -= 1

        if self.count <= self.length // 4:
            self.__shrink()
        return elem


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.enqueue(8)
print(q.elems)
print(q.dequeue())
print(q.dequeue())
q.enqueue(9)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
q.enqueue(10)
print(q.length)




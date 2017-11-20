#coding:utf-8

"""
    假设有n个人围坐一圈，现在从第k个人开始报数，报道第m个人退出，
    然后从下一个人开始继续报道并按同样规则退出，直到所有人退出，
    请按顺序输出各出列人的编号
"""

def josephus_based_list(n, k, m):
    _list = list(range(1, n + 1))
    i = k - 1
    for _ in range(n): # num from 0 to n - 1
        count = 0
        while count < m:
            if _list[i] > 0:
                count += 1
            if count == m:
                print _list[i]
                _list[i] = 0
            i = (i + 1) % n

def josephus_based_list2(n, k, m):
    _list = list(range(1, n + 1))
    i = k - 1
    for j in range(n, 0, -1):
        i = (i + m - 1) % j
        print _list.pop(i)


from exceptions import ValueError

class OverFlow(ValueError):
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
            raise OverFlow('LList Empty')
        if self.rear._next == self.rear:
            self.rear = None
        else:
            self.rear._next = self.rear._next._next

    def pop(self):
        if self.rear == None:
            raise OverFlow('LList Empty')
        elem = self.rear.elem
        if self.rear._next == self.rear:
            self.rear = None
            return elem
        else:
            current = self.rear._next
            while current._next != self.rear:
                current = current._next
            current._next = self.rear._next
            self.rear = current._next
            return elem

class Josephus(CircleLList):

    def turn(self, m):
        for i in range(m):
            self.rear = self.rear._next

    def run(self, n, k, m):
        for i in range(n):
            self.append(i + 1)

        self.turn(k - 1)

        while not self.is_empty():
            self.turn(m - 1)
            print self.pop()


# josephus_based_list2(10, 2, 7)
j = Josephus()
j.run(10, 2, 7)
















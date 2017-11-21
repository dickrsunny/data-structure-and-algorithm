#coding: utf-8

# 递归解
def recursive(n):
    if n == 0:
        return 1
    return n * recursive(n - 1)


class SStack(object):

    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def push(self, elem):
        self.elems.append(elem)

    def pop(self):
        elem = self.elems[-1]
        self.elems.pop()
        return elem


# 非递归解
def non_recursive(n):
    s = SStack()

    for i in range(n, 0, -1):
        s.push(i)

    res = 1
    while not s.is_empty():
        res *= s.pop()

    return res


print recursive(6)
print non_recursive(6)
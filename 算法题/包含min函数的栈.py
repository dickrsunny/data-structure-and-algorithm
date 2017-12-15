#coding: utf-8

"""
定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数

"""


class Solution(object):
    def __init__(self):
        self.elems = []
        self.min_vals = []

    @property
    def is_empty(self):
        return self.elems == []

    def push(self, node):
        # write code here
        self.elems.append(node)
        if not self.min_vals:
            self.min_vals.append(node)
        if node < self.min_vals[-1]:
            self.min_vals.append(node)
        else:
            self.min_vals.append(self.min_vals[-1])

    def pop(self):
        # write code here
        if self.is_empty:
            raise ValueError
        self.elems.pop()
        self.min_vals.pop()

    def top(self):
        # write code here
        if self.is_empty:
            raise ValueError
        return self.elems[-1]

    def min(self):
        # write code here
        if self.is_empty:
            raise ValueError
        return self.min_vals[-1]


class Solution2(object):
    def __init__(self):
        self.elems = []
        self.min_vals = []

    @property
    def is_empty(self):
        return self.elems == []

    def push(self, node):
        # write code here
        self.elems.append(node)
        if not self.min_vals:
            self.min_vals.append(node)
        if node < self.min_vals[-1]:
            self.min_vals.append(node)

    def pop(self):
        # write code here
        if self.is_empty:
            raise ValueError
        elem1 = self.elems[-1]
        elem2 = self.min_vals[-1]
        self.elems.pop()
        self.min_vals.pop()
        if elem1 != elem2:
            self.min_vals.append(elem2)

    def top(self):
        # write code here
        if self.is_empty:
            raise ValueError
        return self.elems[-1]

    def min(self):
        # write code here
        if self.is_empty:
            raise ValueError
        return self.min_vals[-1]


s = Solution()
s.push(1)
s.push(2)
s.push(3)
s.push(1)
s.pop()
print s.min()
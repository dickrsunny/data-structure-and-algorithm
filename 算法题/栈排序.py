#coding: utf-8

"""
    请编写一个程序，按升序对栈进行排序（即最大元素位于栈顶），要求最多只能使用一个额外的栈存放临时数据，但不得将元素复制到别的数据结构中。

    给定一个int[] numbers(C++中为vector&ltint>)，其中第一个元素为栈顶，请返回排序后的栈。请注意这是一个栈，意味着排序过程中你只能访问到第一个元素。

    测试样例：
    [1,2,3,4,5]
    返回：[5,4,3,2,1]
"""

class Stack(object):

    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def top(self):
        return self.elems[-1]

    def push(self, elem):
        self.elems.append(elem)

    def pop(self):
        elem = self.elems[-1]
        self.elems.pop()
        return elem


class TwoStacks(object):

    def twoStacksSort(self, numbers):
        s = Stack()
        numbers_to_s = Stack()

        for i in numbers:
            numbers_to_s.push(i)

        while not numbers_to_s.is_empty():

            top_elem = numbers_to_s.pop()

            if s.is_empty():
                s.push(top_elem)

            elif top_elem <= s.top():
                s.push(top_elem)

            else:
                numbers_to_s.push(s.pop())
                numbers_to_s.push(top_elem)

        while not s.is_empty():
            numbers_to_s.push(s.pop())

        return numbers_to_s


t = TwoStacks()
t.twoStacksSort([6, 3, 8, 1, 2, 5])


# coding: utf-8

"""
输入两个整数序列，第一个序列表示栈的压入顺序，
请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。
例如序列1,2,3,4,5是某栈的压入顺序，序列4，5,3,2,1是该压栈序列对应的一个弹出序列，
但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）

"""


class Stack(object):
    def __init__(self):
        self.elems = []

    @property
    def is_empty(self):
        return self.elems == []

    def push(self, elem):
        self.elems.append(elem)

    def pop(self):
        if self.is_empty:
            raise ValueError
        elem = self.elems[-1]
        self.elems.pop()
        return elem

    def top(self):
        if self.is_empty:
            raise ValueError
        return self.elems[-1]


class Solution(object):

    # 遍历出栈列表
    def IsPopOrder(self, pushV, popV):
        # write code here
        if not pushV or not popV:
            return False

        s = Stack()
        push_pos = 0
        for pop_pos in range(len(popV)):
            pop_elem = popV[pop_pos]
            if pop_elem not in pushV:
                return False

            pos = pushV.index(pop_elem)
            if pos >= push_pos:
                for item in range(push_pos, pos):
                    s.push(pushV[item])
                push_pos = pos + 1
            else:
                if pop_elem != s.pop():
                    return False

        return True

    # 遍历入栈列表（最优解）
    def IsPopOrder2(self, pushV, popV):
        if not pushV or not popV:
            return False

        s = Stack()

        pop_pos = 0
        for item in pushV:
            s.push(item)
            while pop_pos < len(popV) and s.top() == popV[pop_pos]:
                s.pop()
                pop_pos += 1

        return True if s.is_empty else False





s = Solution()
# print s.IsPopOrder2([1, 2, 3, 4, 5], [4, 5, 3, 2, 1])
print s.IsPopOrder([1], [2])

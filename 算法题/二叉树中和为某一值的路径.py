#coding: utf-8
from copy import copy

"""
输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。

"""

class Node(object):

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    # 返回二维列表，内部每个列表表示找到的路径

    def __init__(self):
        self.res = []
        self.temp = []


    def FindPath(self, root, expectNumber):

        if not root:
            return []

        class Stack(object):

            def __init__(self):
                self.elems = []

            @property
            def is_empty(self):
                return self.elems == []

            def push(self, elem):
                self.elems.append(elem)

            def top(self):
                return self.elems[-1]

            def pop(self):
                if self.is_empty:
                    raise ValueError

                elem = self.elems[-1]
                self.elems.pop()
                return elem

        s = Stack()
        s.push((root, False))
        res = []
        temp = []
        while not s.is_empty:
            root, is_right_child = s.pop()
            while root:
                temp.append(root.val)
                if not root.left and not root.right:
                    if sum(temp) == expectNumber:
                        res.append(copy(temp))
                    if is_right_child:
                        temp.pop()
                    temp.pop()
                s.push((root.right, True))
                root = root.left
                is_right_child = False
        return res

    def FindPath2(self, root, expectNumber):
        if not root:
            return []

        self.temp.append(root.val)
        expectNumber -= root.val
        if not root.left and not root.right and expectNumber == 0:
            self.res.append(copy(self.temp))

        self.FindPath2(root.left, expectNumber)
        self.FindPath2(root.right, expectNumber)
        self.temp.pop()
        return self.res






binary_tree = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
s = Solution()
# print s.FindPath(binary_tree, 8)
print s.FindPath2(binary_tree, 8)

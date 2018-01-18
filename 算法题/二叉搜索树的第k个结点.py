#coding: utf-8

"""
给定一颗二叉搜索树，请找出其中的第k大的结点。
例如， 5 / \ 3 7 /\ /\ 2 4 6 8 中，按结点数值大小顺序第三个结点的值为4。

"""

class Stack(object):
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def top(self):
        if self.is_empty():
            raise ValueError()
        return self.elems[-1]

    def push(self, elem):
        self.elems.append(elem)

    def pop(self):
        if self.is_empty():
            raise ValueError()
        elem = self.elems[-1]
        self.elems.pop()
        return elem


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution(object):
    # 返回对应节点TreeNode
    def __init__(self):
        self.count = 0

    def KthNode(self, pRoot, k):
        # write code here
        if not pRoot or not k:
            return

        count = 0
        s = Stack()
        while pRoot or not s.is_empty():
            while pRoot is not None:
                s.push(pRoot)
                pRoot = pRoot.left
            pRoot = s.pop()
            count += 1
            if count == k:
                return pRoot
            pRoot = pRoot.right

    def KthNodeRecursively(self, pRoot, k):
        if not pRoot or not k:
            return

        res = self.KthNodeRecursively(pRoot.left, k)
        if res:
            return res

        self.count += 1
        if self.count == k:
            return pRoot

        res = self.KthNodeRecursively(pRoot.right, k)
        if res:
            return res


t = TreeNode(8, TreeNode(6, TreeNode(5), TreeNode(7)), TreeNode(10, TreeNode(9), TreeNode(11)))
s = Solution()
print s.KthNodeRecursively(t, 1).val
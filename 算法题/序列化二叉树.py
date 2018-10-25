# -*- coding:utf-8 -*-


"""
题目描述

请实现两个函数，分别用来序列化和反序列化二叉树
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self.s_array = []

    def s_pre_order_traverse(self, root, array):
        if not root:
            self.s_array.append("#")
            return

        self.s_array.append(root.val)
        self.s_pre_order_traverse(root.left, array)
        self.s_pre_order_traverse(root.right, array)

    def Serialize(self, root):
        # write code here
        self.s_pre_order_traverse(root, [])
        return self.s_array        

    def d_pre_order_traverse(self, s):
        if s[self.site] == "#":
            return

        node = TreeNode(s[self.site])
        self.site += 1
        node.left = self.d_pre_order_traverse(s)
        self.site += 1
        node.right = self.d_pre_order_traverse(s)
        return node

    def Deserialize(self, s):
        # write code here
        self.site = 0
        return self.d_pre_order_traverse(s)


s = Solution()
root = s.Deserialize("124###3##")
print(s.Serialize(root))

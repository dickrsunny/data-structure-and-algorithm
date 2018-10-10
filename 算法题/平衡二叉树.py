"""
输入一棵二叉树，判断该二叉树是否是平衡二叉树。
"""

"""
思路：平衡二叉树满足对于任意子树其左右孩子的高度差的绝对值要小于等于1；
下面的代码实则为求树高的变形
"""

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.is_balance = True

    def height(self, root):
        if root is None:
            return 0

        left = self.height(root.left)
        right = self.height(root.right)

        if abs(left - right) > 1:
            self.is_balance = False

        return max(left, right) + 1

    def IsBalanced_Solution(self, pRoot):
        # write code here
        self.height(pRoot)
        return self.is_balance

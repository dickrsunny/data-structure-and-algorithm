#coding: utf-8


"""

请实现一个函数，用来判断一颗二叉树是不是对称的。
注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。

"""


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def do_detail(self, root1, root2):
        if not root1 and not root2:
            return True

        if not root1 or not root2:
            return False

        if root1.val != root2.val:
            return False

        return self.do_detail(root1.left, root2.right) and self.do_detail(root1.right, root2.left)

    def isSymmetrical(self, pRoot):
        # write code her

        return self.do_detail(pRoot, pRoot)




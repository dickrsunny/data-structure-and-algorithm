#coding: utf-8

"""
输入两棵二叉树A，B，判断B是不是A的子结构。
（ps：我们约定空树不是任意一个树的子结构）

"""


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def is_same_tree(self, root1, root2):
        if not root1 and not root2:
            return True
        elif root1 and not root2:
            return True
        elif root1 and root2:
            return root1.val == root2.val and self.is_same_tree(root1.left, root2.left) and self.is_same_tree(
                root1.right, root2.right)
        else:
            return False

    # 找到pRoot1中pRoot2的位置，再进行比较
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
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

        if not pRoot1 or not pRoot2:
            return False

        s = Stack()
        s.push(pRoot1)
        flag = False
        while not s.is_empty:
            if flag == True:
                break
            root = s.pop()
            while root:
                if root.val == pRoot2.val:
                    if self.is_same_tree(root, pRoot2):
                        flag = True
                        break
                s.push(root.right)
                root = root.left
        return flag

    def HasSubtree_recursively(self, pRoot1, pRoot2):
        flag = False
        if not pRoot1 or not pRoot2:
            return flag

        if pRoot1.val == pRoot2.val:
            flag = self.is_same_tree(pRoot1, pRoot2)
        if not flag:
            flag = self.HasSubtree(pRoot1.left, pRoot2)
        if not flag:
            flag = self.HasSubtree(pRoot1.right, pRoot2)
        return flag

    # 利用好短路特性，完全不用那么多flag
    def HasSubtree2(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
            return False

        return self.is_same_tree(pRoot1, pRoot2) or self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(
            pRoot1.right, pRoot2)
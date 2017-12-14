#coding: utf-8

"""
操作给定的二叉树，将其变换为源二叉树的镜像:
    二叉树的镜像定义：
        源二叉树
    	    8
    	   /  \
    	  6   10
    	 / \  / \
    	5  7 9 11

    	镜像二叉树
    	    8
    	   /  \
    	  10   6
    	 / \  / \
    	11 9 7  5

"""


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def Mirror(self, root):
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

        if not root:
            return

        s = Stack()
        s.push(root)
        while not s.is_empty:
            root = s.pop()
            while root:
                root.left, root.right = root.right, root.left
                s.push(root.right)
                root = root.left
        return root

    def mirror_pre_order_recursively(self, root):
        # write code here
        if not root:
            return

        root.left, root.right = root.right, root.left
        self.mirror_pre_order_recursively(root.left)
        self.mirror_pre_order_recursively(root.right)
        return root

    def mirror_in_order_recursively(self, root):
        if not root:
            return

        self.mirror_in_order_recursively(root.left)
        root.left, root.right = root.right, root.left
        self.mirror_in_order_recursively(root.left)
        return root

    def mirror_post_order_recursively(self, root):
        if not root:
            return

        self.mirror_post_order_recursively(root.left)
        self.mirror_post_order_recursively(root.right)
        root.left, root.right = root.right, root.left
        return root
#coding: utf-8

"""
从上到下按层打印二叉树，
同一层结点从左至右输出。每一层输出一行。

"""


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next_ = None


class CircleLinkedList(object):
    def __init__(self):
        self.rear = None

    @property
    def is_empty(self):
        return self.rear == None

    def append(self, elem):
        node = Node(elem)
        if self.is_empty:
            self.rear = node
            node.next_ = node
        else:
            next_ = self.rear.next_
            self.rear.next_ = node
            node.next_ = next_
            self.rear = node

    def prepop(self):
        if self.is_empty:
            raise ValueError
        elem = self.rear.next_.elem
        if self.rear.next_ == self.rear:
            self.rear = None
        else:
            self.rear.next_ = self.rear.next_.next_
        return elem

    def size(self):
        if self.is_empty:
            return 0
        current = self.rear.next_
        count = 1
        while current != self.rear:
            count += 1
            current = current.next_
        return count

    def last(self):
        if not self.is_empty:
            return self.rear.elem


class Queue(CircleLinkedList):
    def enqueue(self, elem):
        self.append(elem)

    def dequeue(self):
        return self.prepop()


class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        q = Queue()
        q.enqueue(pRoot)
        last = pRoot
        res, tmp = [], []
        while not q.is_empty:
            root = q.dequeue()
            if root.left:
                q.enqueue(root.left)
            if root.right:
                q.enqueue(root.right)
            tmp.append(root.val)
            if root == last:
                res.append(tmp)
                tmp = []
                last = q.last()
        return res


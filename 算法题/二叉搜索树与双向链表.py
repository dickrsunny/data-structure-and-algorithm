#coding: utf-8

"""
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向

"""


class Solution(object):

    def __init__(self):
        self.head = None
        self.prev = None

    def Convert(self, pRootOfTree):
        # write code here
        self.detail(pRootOfTree)
        return self.head

    # 每次只交换前后两个节点的一对链接
    def detail(self, root):
        if not root:
            return

        self.detail(root.left)

        if not self.head:
            self.head = self.prev = root
        else:
            self.prev.right = root
            root.left = self.prev
            self.prev = root

        self.detail(root.right)

    def Convert2(self, pRootOfTree):
        class Stack(object):

            def __init__(self):
                self.elems = []

            @property
            def is_empty(self):
                return self.elems == []

            def top(self):
                if self.is_empty:
                    raise ValueError
                return self.elems[-1]

            def push(self, elem):
                self.elems.append(elem)

            def pop(self):
                if self.is_empty:
                    raise ValueError
                elem = self.elems[-1]
                self.elems.pop()
                return elem

        prev = head = None
        s = Stack()
        while pRootOfTree or not s.is_empty:
            while pRootOfTree:
                s.push(pRootOfTree)
                pRootOfTree = pRootOfTree.left
            pRootOfTree = s.pop()
            if not head:
                prev = head = pRootOfTree
            else:
                prev.right = pRootOfTree
                pRootOfTree.left = prev
                prev = pRootOfTree
            pRootOfTree = pRootOfTree.right
        return head
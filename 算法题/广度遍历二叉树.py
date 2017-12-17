#coding: utf-8

class BinaryTreeNode(object):

    def __init__(self, elem, left=None, right=None):
        self.elem = elem
        self.left = left
        self.right = right


class Solution(object):
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []

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

        class Queue(CircleLinkedList):

            def enqueue(self, elem):
                self.append(elem)

            def dequeue(self):
                return self.prepop()

        q = Queue()
        q.enqueue(root)
        res = []
        while not q.is_empty:
            root = q.dequeue()
            res.append(root.elem)
            if root.left:
                q.enqueue(root.left)
            if root.right:
                q.enqueue(root.right)
        return res

binary_tree = BinaryTreeNode(1, BinaryTreeNode(2, BinaryTreeNode(4), BinaryTreeNode(5)), BinaryTreeNode(3, BinaryTreeNode(6), BinaryTreeNode(7)))
s = Solution()
print s.PrintFromTopToBottom(binary_tree)
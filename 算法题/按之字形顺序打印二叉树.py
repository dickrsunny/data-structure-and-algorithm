#coding: utf-8

"""
请实现一个函数按照之字形打印二叉树，
即第一行按照从左到右的顺序打印，
第二层按照从右至左的顺序打印，
第三行按照从左到右的顺序打印，其他行以此类推

"""

class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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


class Solution(object):
    def Print(self, pRoot):
        if not pRoot:
            return []

        class Stack(object):

            def __init__(self):
                self.elems = []

            @property
            def is_empty(self):
                return self.elems == []

            def push(self, val):
                self.elems.append(val)

            def pop(self):
                if self.is_empty:
                    raise ValueError
                elem = self.elems[-1]
                self.elems.pop()
                return elem

            def size(self):
                return len(self.elems)

        q = Queue()
        q.enqueue(pRoot)
        s = Stack()
        count, next_level_count, depth = 0, 1, 0
        left_to_right = True
        res, temp = [], []
        while not q.is_empty:
            root = q.dequeue()

            if root.left:
                q.enqueue(root.left)
            if root.right:
                q.enqueue(root.right)
            if left_to_right:
                if root.left:
                    s.push(root.left)
                if root.right:
                    s.push(root.right)
            else:
                root = s.pop()
            count += 1
            temp.append(root.val)
            if count == next_level_count:
                res.append(temp)
                temp = []
                count = 0
                next_level_count = q.size()
                left_to_right = not left_to_right
        return res


    def Print2(self, pRoot):
        # write code here
        if not pRoot:
            return []

        q = Queue()
        q.enqueue(pRoot)
        left_to_right = True
        # count, next_level_count= 0, 1
        last = pRoot
        res, temp = [], []
        while not q.is_empty:
            root = q.dequeue()

            if root.left:
                q.enqueue(root.left)
            if root.right:
                q.enqueue(root.right)

            temp.append(root.val)
            # count += 1
            if root == last:
                if not left_to_right:
                    temp = temp[::-1]
                res.append(temp)
                temp = []
                left_to_right = not left_to_right
                last = q.last()
        return res







t = TreeNode(8, TreeNode(6, TreeNode(5), TreeNode(7)), TreeNode(10, TreeNode(9), TreeNode(11)))
s = Solution()
print s.Print(t)



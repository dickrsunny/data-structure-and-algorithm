# coding: utf-8

class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution(object):
    def tree_depth(self, pRoot):

        if pRoot == None:
            return 0

        class Node(object):
            def __init__(self, val):
                self.val = val
                self.next_ = None

        class CircleSingleLinkedList(object):

            def __init__(self):
                self.rear = None

            @property
            def is_empty(self):
                return self.rear == None

            def push(self, val):
                node = Node(val)
                if self.is_empty:
                    self.rear = node
                    self.rear.next_ = self.rear
                else:
                    elem = self.rear.next_
                    self.rear.next_ = node
                    node.next_ = elem
                    self.rear = node

            def pop(self):
                if self.is_empty:
                    raise ValueError
                elem = self.rear.next_
                if elem == self.rear:
                    self.rear = None
                else:
                    self.rear.next_ = elem.next_
                return elem.val

            def size(self):
                if self.is_empty:
                    return 0
                current, count = self.rear.next_, 1
                while current != self.rear:
                    count += 1
                    current = current.next_
                return count

        class Queue(CircleSingleLinkedList):

            def enqueue(self, val):
                self.push(val)

            def dequeue(self):
                return self.pop()

        q = Queue()
        q.enqueue(pRoot)
        count, next_level_count, depth = 0, 1, 0
        while not q.is_empty:
            root = q.dequeue()
            if root.left:
                q.enqueue(root.left)
            if root.right:
                q.enqueue(root.right)
            count += 1
            if count == next_level_count:
                depth += 1
                next_level_count = q.size()
                count = 0
        return depth


    def TreeDepthRecursively(self, pRoot):
        # write code here
        if pRoot == None:
            return 0

        return max(self.TreeDepthRecursively(pRoot.left), self.TreeDepthRecursively(pRoot.right)) + 1


t = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
s = Solution()
print s.tree_depth(t)

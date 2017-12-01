#coding: utf-8

class Node(object):

    def __init__(self, elem, left=None, right=None):
        self.elem = elem
        self.left = left
        self.right = right


# 统计二叉树节点数量
def count(binary_tree):
    if binary_tree == None:
        return 0
    return 1 + count(binary_tree.left) + count(binary_tree.right)


# 二叉树节点元素之和
def sum(binary_tree):
    if binary_tree == None:
        return 0
    return binary_tree.elem + sum(binary_tree.left) + sum(binary_tree.right)


# 深度遍历：先序遍历，中序遍历，后续遍历

# 先序遍历
def pre_order_traverse(binary_tree):
    if binary_tree == None:
        return
    print binary_tree.elem
    pre_order_traverse(binary_tree.left)
    pre_order_traverse(binary_tree.right)


from exceptions import ValueError

class UnderFlow(ValueError):
    pass

class Stack(object):

    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def top(self):
        if self.is_empty():
            raise UnderFlow('Stack is empty')
        return self.elems[-1]

    def push(self, elem):
        self.elems.append(elem)

    def pop(self):
        if self.is_empty():
            raise UnderFlow('Stack is empty')
        elem = self.elems[-1]
        self.elems.pop()
        return elem


def pre_order_traverse_non_recursively(binary_tree):
    s = Stack()
    while binary_tree or not s.is_empty():
        while binary_tree:
            print binary_tree.elem
            s.push(binary_tree.right)
            binary_tree = binary_tree.left
        binary_tree = s.pop()


# 中序遍历
def in_order_traverse(binary_tree):
    if binary_tree == None:
        return
    in_order_traverse(binary_tree.left)
    print binary_tree.elem
    in_order_traverse(binary_tree.right)


def in_order_traverse_non_recursively(binary_tree):
    s = Stack()
    while binary_tree is not None or not s.is_empty():
        while binary_tree is not None:
            s.push(binary_tree)
            binary_tree = binary_tree.left
        binary_tree = s.pop()
        print binary_tree.elem
        binary_tree = binary_tree.right


# 后续遍历
def back_order_traverse(binary_tree):
    if binary_tree == None:
        return
    back_order_traverse(binary_tree.left)
    back_order_traverse(binary_tree.right)
    print binary_tree.elem


def back_order_traverse_non_recursively(binary_tree):
    s = Stack()
    while binary_tree or not s.is_empty():
        while binary_tree:
            s.push(binary_tree)
            binary_tree = binary_tree.left if binary_tree else binary_tree.right

        binary_tree = s.pop()
        print binary_tree.elem
        if not s.is_empty() and s.top().left == binary_tree:
            binary_tree = s.top().right
        else:
            binary_tree = None


# 广度遍历
def level_order_traverse(binary_tree):

    from exceptions import Exception

    class UnderFlow(Exception):
        pass

    class Queue(object):

        def __init__(self, length=4):
            self.length = length
            self.elems = [0] * length
            self.head = 0
            self.count = 0

        def is_empty(self):
            return self.count == 0

        def peek(self):
            if self.is_empty():
                raise UnderFlow()
            return self.elems[self.head]

        def dequeue(self):
            if self.is_empty():
                raise UnderFlow()
            elem = self.elems[self.head]
            self.head = (self.head + 1) % self.length
            self.count -= 1
            return elem

        def __expand(self):
            new_length = self.length * 2
            list_ = [0] * new_length
            for i in range(self.length):
                list_[i] = self.elems[(self.head + i) % self.length]
            self.elems = list_
            self.head = 0
            self.length = new_length

        def enqueue(self, elem):
            if self.count == self.length:
                self.__expand()
            self.elems[(self.head + self.count) % self.length] = elem
            self.count += 1

    q = Queue()
    q.enqueue(binary_tree)
    while not q.is_empty():
        t = q.dequeue()
        print t.elem
        if t.left != None:
            q.enqueue(t.left)
        if t.right != None:
            q.enqueue(t.right)


# 最大树深
def max_depth(binary_tree):
    if binary_tree == None:
        return 0
    return max(max_depth(binary_tree.left), max_depth(binary_tree.right)) + 1




binary_tree = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
# print count(binary_tree)
# print sum(binary_tree)
# pre_order_traverse_non_recursively(binary_tree)
# in_order_traverse_non_recursively(binary_tree)
back_order_traverse_non_recursively(binary_tree)
# level_order_traverse(binary_tree)
# print max_depth(binary_tree)

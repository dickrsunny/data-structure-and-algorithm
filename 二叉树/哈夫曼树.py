#coding: utf-8

class BinaryTreeNode(object):

    def __init__(self, elem, left=None, right=None):
        self.elem = elem
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.elem < other.elem


from exceptions import Exception


class UnderFlow(Exception):
    pass


class PriorityQueue(object):

    def __init__(self, list_=None):
        self.elems = list_
        if self.elems:
            self.heapify()

    def heapify(self):
        length = len(self.elems)
        for i in range(length // 2 - 1, -1, -1):
            self.sift_down(length, i)
            # self.sift_down_recursively(length, i)

    def is_empty(self):
        return self.elems == None

    def number(self):
        return len(self.elems)

    def peek(self):
        if self.is_empty():
            raise UnderFlow()
        return self.elems[0]

    def enqueue(self, elem):
        self.elems.append(elem)
        elem_site = len(self.elems) - 1
        self.sift_up(elem_site)

    def sift_up(self, elem_site):
        while True:
            parent_site = elem_site // 2
            if self.elems[elem_site] < self.elems[parent_site]:
                temp = self.elems[elem_site]
                self.elems[elem_site] = self.elems[parent_site]
                self.elems[parent_site] = temp
                elem_site = parent_site
            else:
                break

    def dequeue(self):
        first_elem = self.elems[0]
        last_elem = self.elems[-1]
        self.elems[0] = last_elem
        self.elems.pop()
        self.sift_down(len(self.elems), 0)
        return first_elem

    def sift_down(self, length, root_site):
        while True:
            left_child = root_site * 2 + 1
            right_child = root_site * 2 + 2
            if left_child < length and self.elems[left_child] < self.elems[root_site]:
                self.elems[root_site], self.elems[left_child] = self.elems[left_child], self.elems[root_site]
                root_site = left_child
            elif right_child < length and self.elems[right_child] < self.elems[root_site]:
                self.elems[root_site], self.elems[right_child] = self.elems[right_child], self.elems[root_site]
                root_site = right_child
            else:
                break

def HaffmanTree(weights):
    q = PriorityQueue([])
    for i in weights:
        q.enqueue(BinaryTreeNode(i))
    while q.number() > 1:
        w1 = q.dequeue()
        w2 = q.dequeue()
        add = w1.elem + w2.elem
        q.enqueue(BinaryTreeNode(add, w1, w2))
    return q.dequeue()


print HaffmanTree([2, 3, 7, 10, 4, 2, 5]).left.elem



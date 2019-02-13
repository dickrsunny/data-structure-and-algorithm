# coding: utf-8
"""
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

    def peek(self):
        if self.is_empty():
            raise UnderFlow()
        return self.elems[0]

    def enqueue(self, elem):
        self.elems.append(elem)
        elem_site = len(self.elems) - 1
        self.sift_up(elem_site)
        # self.sift_up_recursively(elem_site)

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

    def sift_up_recursively(self, elem_site):
        parent_site = elem_site // 2
        if self.elems[elem_site] >= self.elems[parent_site]:
            return

        temp = self.elems[elem_site]
        self.elems[elem_site] = self.elems[parent_site]
        self.elems[parent_site] = temp
        self.sift_up_recursively(parent_site)

    def dequeue(self):
        first_elem = self.elems[0]
        last_elem = self.elems[-1]
        self.elems[0] = last_elem
        self.elems.pop()
        self.sift_down(len(self.elems), 0)
        # self.sift_down_recursively(len(self.elems), 0)
        return first_elem

    def sift_down(self, length, root_site):
        while root_site * 2 + 1 < length:
            left_site = root_site * 2 + 1
            right_site = root_site * 2 + 2

            if right_site < length and self.elems[left_site] > self.elems[right_site]:
                left_site = right_site

            if self.elems[root_site] > self.elems[left_site]:
                self.elems[root_site], self.elems[left_site] = self.elems[left_site], self.elems[root_site]
            else:
                break

            root_site = left_site

    def sift_down_recursively(self, length, root_site):
        left_child = root_site * 2 + 1
        right_child = root_site * 2 + 2
        min_val_site = root_site
        if left_child < length and self.elems[min_val_site] > self.elems[left_child]:
            min_val_site = left_child

        if right_child < length and self.elems[min_val_site] > self.elems[right_child]:
            min_val_site = right_child

        if min_val_site != root_site:
            self.elems[root_site], self.elems[min_val_site] = self.elems[min_val_site], self.elems[root_site]
            self.sift_down_recursively(length, min_val_site)


p = PriorityQueue([1, 2, 7, 5, 2, 9, 3])
print p.elems
p.dequeue()
print p.elems
"""


class PriorityQueue(object):

    def __init__(self, list_=None):
        if list_ is None:
            list_ = []
        self.elems = list_
        if self.elems:
            self.heapify()

    @property
    def is_empty(self):
        return self.elems == []

    def heapify(self):
        half = len(self.elems) // 2 - 1
        for i in range(half, -1, -1):
            self.sift_down(i)

    def sift_down(self, root_site):
        length = len(self.elems)
        while 2 * root_site + 1 < length:
            left_site = 2 * root_site + 1
            right_site = 2 * root_site + 2

            if right_site < length and self.elems[left_site] < self.elems[right_site]:
                left_site = right_site

            if self.elems[root_site] < self.elems[left_site]:
                self.elems[root_site], self.elems[left_site] = self.elems[left_site], self.elems[root_site]
            else:
                break

            root_site = left_site

    def dequeue(self):
        if self.is_empty:
            raise ValueError()

        elem = self.elems[0]
        self.elems[0], self.elems[-1] = self.elems[-1], self.elems[0]
        self.elems.pop()

        if len(self.elems) > 1:
            self.sift_down(0)
        return elem

    def enqueue(self, val):
        self.elems.append(val)
        if len(self.elems) > 1:
            self.sift_up()

    def sift_up(self):
        site = len(self.elems) - 1
        while site > 0 and self.elems[site] > self.elems[(site - 1) // 2]:
            self.elems[site], self.elems[(site - 1) // 2] = self.elems[(site - 1) // 2], self.elems[site]
            site = (site - 1) // 2


# q = PriorityQueue([6, 5, 7, 2, 9, 3, 1])
q = PriorityQueue([6, 5, 7, 2, 9, 3])
print(q.elems)
# p.dequeue()
q.enqueue(10)
print(q.elems)

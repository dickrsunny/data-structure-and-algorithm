#coding: utf-8
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
        # self.sift_down()
        self.sift_down_recursively(len(self.elems), 0)
        return first_elem

    def sift_down(self, length, root_site):
        while True:
            left_child = root_site * 2 + 1
            right_child = root_site * 2 + 2
            if left_child < length and self.elems[root_site] > self.elems[left_child]:
                self.elems[root_site], self.elems[left_child] = self.elems[left_child], self.elems[root_site]
                root_site = left_child
            elif right_child < length and self.elems[root_site] > self.elems[right_child]:
                self.elems[root_site], self.elems[right_child] = self.elems[right_child], self.elems[root_site]
                root_site = right_child
            else:
                break

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

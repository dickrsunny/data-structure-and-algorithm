#coding: utf-8
from exceptions import ValueError

class UnderFlow(ValueError):
    pass

class LNode(object):
    def __init__(self, elem, _next=None):
        self.elem = elem
        self._next = None


class LListWithTailNode(object):

    def __init__(self):
        self.head = None
        self.rear = None

    def is_empty(self):
        return self.head == None

    def prepend(self, elem):
        n = LNode(elem)
        if self.is_empty():
            self.head = n
            self.rear = n
        else:
            n._next = self.head
            self.head = n

    def append(self, elem):
        n = LNode(elem)
        if self.is_empty():
            self.head = n
            self.rear = n
        else:
            self.rear._next = n
            self.rear = n

    def prepop(self):
        if self.is_empty():
            raise UnderFlow('LList is empty')
        current = self.head
        if current._next == None:
            elem = self.head.elem
            self.head = None
            self.rear = None
            return elem
        else:
            elem = self.head.elem
            self.head = self.head._next
            return elem

    def pop(self):
        if self.is_empty():
            raise UnderFlow('LList is empty')
        current = self.head
        if current._next == None:
            elem = self.head.elem
            self.head = None
            self.rear = None
            return elem
        else:
            while current._next._next != None:
                current = current._next
            elem = current._next.elem
            current._next = None
            self.rear = current
            return elem

    def traverse(self, head=None):
        current = head or self.head
        while current != None:
            print current.elem
            current = current._next

    # 每次只改变当前节点的链接指向
    def reverse(self):
        prev = None
        current = self.head
        while current != None:
            next_node = current._next
            current._next = prev
            prev = current
            current = next_node
        self.head = prev

    def recursive_reverse(self, head=None):
        if head == None:
            return

        if head._next == None:
            return head

        new_head = self.recursive_reverse(head._next)
        head._next._next = head
        head._next = None
        self.head = new_head
        return new_head

    # 插入排序
    def sort(self):
        next_node = self.head._next
        while next_node != None:
            current = self.head
            while current != next_node:
                if next_node.elem < current.elem:
                    temp = next_node.elem
                    next_node.elem = current.elem
                    current.elem = temp
                current = current._next
            next_node = next_node._next

    # 交换成对链表元素
    def swap_pairs_elem(self):
        current = self.head
        while current and current._next:
            temp = current.elem
            current.elem = current._next.elem
            current._next.elem = temp
            if current._next._next:
                current = current._next._next
            else:
                break

    # 交换成对链表链接
    def swap_pairs_link(self):
        current = self.head
        self.head = current._next
        prev = None
        while current and current._next:
            temp = current._next
            current._next = current._next._next
            temp._next = current
            if prev:
                prev._next = temp
            if current._next:
                prev = current
                current = current._next
            else:
                break

    # 递归交换成对链表
    def swap_pairs_link_recursively(self, head):
        current = head
        if current != None and current._next != None:
            temp = current._next
            current._next = self.swap_pairs_link_recursively(temp._next)
            temp._next = current
            return temp
        return current


# 交叉链表求交点
def cross_node(l1, l2):
    if not l1.is_empty() and not l2.is_empty():
        length1, length2 = 1, 1
        current1 = head1 = l1.head
        while current1._next != None:
            length1 += 1
            current1 = current1._next
        current2 = head2 = l2.head
        while current2._next != None:
            length2 += 1
            current2 = current2._next
        if current1.elem == current2.elem:
            if length1 >= length2:
                for i in range(length1 - length2):
                    head1 = head1._next
            else:
                for i in range(length2 - length1):
                    head2 = head2._next
            while head1 and head2:
                if head1.elem == head2.elem:
                    return head1.elem
                head1 = head1._next
                head2 = head2._next
    print '无交点'


l = LListWithTailNode()
l2 = LListWithTailNode()
l.append(5)
l.append(6)
l.append(1)
l.append(2)
# l.traverse()
l2.append(3)
l2.append(4)
l2.append(7)
l2.append(8)
l2.append(1)
l2.append(2)
# l2.traverse()
print cross_node(l, l2)
# l.sort()
# l.traverse()
# print ''
# l.recursive_reverse(l.head)
# print l.rear.elem, '\n'
# l.append(5)
# l.append(6)
# l.traverse()
# print l.rear.elem
# res = l.swap_pairs_link_recursively(l.head)
# l.traverse(res)




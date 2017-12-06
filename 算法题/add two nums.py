#coding: utf-8
"""
Complexity Analysis

Time complexity : O(max(m, n)). Assume that m and n represents the length of l1 and l2 respectively, the algorithm above iterates at most max(m,n) times.

Space complexity : O(max(m, n)). The length of the new list is at most max(m,n) +1.

详情请参考：https://leetcode.com/problems/add-two-numbers/solution/
"""


"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

"""

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


class Solution(object):
    def addTwoNumbers(self, l1, l2):

        l3 = LListWithTailNode()
        carry = 0
        while l1 or l2 or carry:
            num1 = l1.elem
            l1 = l1._next

            num2 = l2.elem
            l2 = l2._next

            carry, val = divmod(num1 + num2 + carry, 10)

            l3.append(val)
        return l3


l1 = LListWithTailNode()
l1.append(2)
l1.append(4)
l1.append(3)

l2 = LListWithTailNode()
l2.append(5)
l2.append(6)
l2.append(4)

s = Solution()
s.addTwoNumbers(l1.head, l2.head).traverse()


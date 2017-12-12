# coding: utf-8

"""
输入一个链表，输出该链表中倒数第k个结点。

"""


# 常规解法要么是 > O(n) 的时间复杂度，或 O(n)的时间复杂度
# eg:


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def FindKthToTail(self, head, k):
        # write code here
        if k > 0 and head:
            length = 0
            current = head
            while current != None:
                length += 1
                current = current.next
            if k <= length:
                for i in range(length - k):
                    head = head.next
                return head


# 最优解：时间复杂度：O(n)，空间复杂度：O(1)
class Solution2(object):
    def FindKthToTail(self, head, k):
        # write code here
        if k > 0 and head:
            first = head
            for i in range(k - 1):
                first = first.next
            if first != None:
                second = head
                while first.next != None:
                    first = first.next
                    second = second.next
                return second

#coding: utf-8

"""
输入两个链表，找出它们的第一个公共结点。

"""


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2:
            return
        current1 = pHead1
        length1 = 0
        while current1:
            length1 += 1
            current1 = current1.next

        current2 = pHead2
        length2 = 0
        while current2:
            length2 += 1
            current2 = current2.next

        if length1 > length2:
            for _ in range(length1 - length2):
                pHead1 = pHead1.next
        else:
            for _ in range(length2 - length1):
                pHead2 = pHead2.next

        while pHead1:
            if pHead1.val == pHead2.val:
                return pHead1
            pHead1 = pHead1.next
            pHead2 = pHead2.next
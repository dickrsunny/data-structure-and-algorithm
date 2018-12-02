# coding: utf-8

"""
https://leetcode.com/problems/reverse-linked-list/
题目描述：
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
"""


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        prev = None
        current = head
        while current:
            next_ = current.next
            current.next = prev
            prev = current
            current = next_

        head = prev

        return head

    def reverseList_recursively(self, head):
        if not head or not head.next:
            return head

        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return new_head

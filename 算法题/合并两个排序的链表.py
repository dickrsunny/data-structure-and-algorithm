#coding: utf-8

"""
输入两个单调递增的链表，输出两个链表合成后的链表，
当然我们需要合成后的链表满足单调不减规则

"""

class ListNode(object):

    def __init__(self, x, y=None):
        self.val = x
        self.next = y


class Solution(object):

    def merge_two_sorted_list(self, pHead1, pHead2):
        # current = head = ListNode(0)
        # current1, current2 = pHead1, pHead2
        #
        # while current1 and current2:
        #     if current1.val <= current2.val:
        #         current.next = current1
        #         current1 = current1.next
        #     else:
        #         current.next = current2
        #         current2 = current2.next
        #     current = current.next
        #
        # if current1:
        #     current.next = current1
        # else:
        #     current.next = current2
        # return head.next

        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1

        current1, current2 = pHead1, pHead2
        if current1.val <= current2.val:
            head = current = current1
            current1 = current1.next
        else:
            head = current = current2
            current2 = current2.next

        while current1 and current2:
            if current1.val <= current2.val:
                current.next = current1
                current1 = current1.next
            else:
                current.next = current2
                current2 = current2.next
            current = current.next

        if current1:
            current.next = current1
        else:
            current.next = current2
        return head

    def merge_two_sorted_list_recursively(self, pHead1, pHead2):
        if not pHead1:
            return pHead2

        if not pHead2:
            return pHead1

        if pHead1.val <= pHead2.val:
            pHead1.next = self.merge_two_sorted_list_recursively(pHead1.next, pHead2)
            return pHead1
        else:
            pHead2.next = self.merge_two_sorted_list_recursively(pHead1, pHead2.next)
            return pHead2


l1 = ListNode(1, ListNode(3, ListNode(5)))
l2 = ListNode(2, ListNode(4, ListNode(6)))

s = Solution()
print s.merge_two_sorted_list_recursively(l1, l2).val

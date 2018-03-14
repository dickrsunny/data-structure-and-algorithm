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


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        current1, current2 = l1, l2
        decade = 0
        res = []
        while current1 or current2:
            if current1 and current2:
                _sum = current1.val + current2.val + decade
                current1 = current1.next
                current2 = current2.next
            elif current1:
                _sum = current1.val + decade
                current1 = current1.next

            else:
                _sum = current2.val + decade
                current2 = current2.next

            unit = _sum % 10
            decade = (_sum // 10) % 10

            res.append(unit)
            if not current1 and not current2 and decade:
                res.append(decade)
        return res
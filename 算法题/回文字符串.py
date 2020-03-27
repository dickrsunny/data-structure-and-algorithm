"""
https://leetcode.com/problems/palindrome-linked-list/
题目描述：
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""

"""
解题思路：
1: Reverse the first half while finding the middle.
2: Compare the reversed first half with the second half.
"""


class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True

        prev = None
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next  # 此行和下面的语句位置不能互换，因为修改slow的同时会修改fast
            next_ = slow.next
            slow.next = prev
            prev = slow
            slow = next_

        if fast:
            slow = slow.next

        while slow:
            if slow.val != prev.val:
                return False

            slow = slow.next
            prev = prev.next

        return True

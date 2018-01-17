#coding: utf-8

"""
一个链表中包含环，请找出该链表的环的入口结点

"""

"""
解题思路：
    1. 第一步，找环中相汇点。分别用p1，p2指向链表头部，
       p1每次走一步，p2每次走二步，直到p1==p2找到在环中的相汇点。
       
    2. 第二步，找环的入口。接上步，当p1==p2时，p2所经过节点数为2x,
       p1所经过节点数为x,设环中有n个节点,p2比p1多走一圈有2x=n+x; n=x;
       可以看出p1实际走了一个环的步数，再让p2指向链表头部，p1位置不变，
       p1,p2每次走一步直到p1==p2; 此时p1指向环的入口。

"""

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    # 时间复杂度：O(n)   空间复杂度：O(n)
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return

        current = pHead
        nodes = set()
        while current:
            if current in nodes:
                return current
            nodes.add(current)
            current = current.next

    # 时间复杂度：O(n)  空间复杂度：O(1)
    def EntryNodeOfLoop2(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return

        p1, p2 = pHead, pHead
        while p1:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                p2 = pHead
                while p1 != p2:
                    p1 = p1.next
                    p2 = p2.next
                return p1


#coding: utf-8

"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级。
求该青蛙跳上一个n级的台阶总共有多少种跳法?

"""

class Solution(object):
    def jumpFloor(self, number):
        # write code here
        i, j = 0, 1
        for _ in range(number):
            i, j = j, i + j
        return j

s = Solution()
print s.jumpFloor(6)

# coding: utf-8

"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。
求该青蛙跳上一个n级的台阶总共有多少种跳法?

"""


# 递归解

class Solution(object):
    def jumpFloorII(self, number):
        # write code here
        if number <= 0:
            return -1
        elif number == 1:
            return 1
        else:
            return 2 * self.jumpFloorII(number - 1)


# 非递归解

class Solution2(object):
    def jumpFloorII(self, number):
        return 2 ** (number - 1)


s = Solution()
print s.jumpFloorII(6)
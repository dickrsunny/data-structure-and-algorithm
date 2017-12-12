#coding: utf-8

"""
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示

"""

class Solution(object):
    def NumberOf1(self, n):
        # write code here
        count = 0
        for i in range(32):
            count +=  (n >> i) & 1
        return count

s = Solution()
print s.NumberOf1(66)
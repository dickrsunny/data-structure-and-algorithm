#coding: utf-8

"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前半部分，所有的偶数位于位于数组的后半部分，
并保证奇数和奇数，偶数和偶数之间的相对位置不变。

"""


class Solution(object):
    def reOrderArray(self, array):
        # write code here
        odd = []
        even = []
        for i in array:
            if i % 2 == 1:
                odd.append(i)
            else:
                even.append(i)
        return odd + even

s = Solution()
print s.reOrderArray([1, 2, 3, 4, 5, 6])
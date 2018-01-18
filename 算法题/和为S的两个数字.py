# coding: utf-8

"""
题目描述：
输入一个递增排序的数组和一个数字S，
在数组中查找两个数，是的他们的和正好是S，
如果有多对数字的和等于S，输出两个数的乘积最小的。

输出描述:
对应每个测试案例，输出两个数，小的先输出。

"""


class Solution(object):

    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if not array or tsum <= array[0]:
            return []

        low, high = 0, len(array) - 1
        while low < high:
            if array[low] + array[high] < tsum:
                low += 1
            elif array[low] + array[high] > tsum:
                high -= 1
            else:
                return [array[low], array[high]]
        return []


s = Solution()
print s.FindNumbersWithSum([1, 2, 4, 7, 11, 16], 11)

#coding: utf-8

"""
题目描述：
在一个二维数组中，每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。请完成一个函数，
输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

"""


class Solution(object):
    def Find(self, target, array):
        # write code here
        column, row = len(array), len(array[0])
        i, j = 0, row - 1
        while i < column and j >= 0:
            if target == array[i][j]:
                return True
            elif target > array[i][j]:
                i += 1
            else:
                j -= 1
        return False

s = Solution()
print s.Find(6, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
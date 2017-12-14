# coding: utf-8

"""
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.

"""

"""
            top
            
        1  2  3  4
        5  6  7  8   
 left   9  10 11 12   right
        13 14 15 16
        
            bottom
"""


class Solution(object):
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if not matrix or not matrix[0]:
            return matrix

        row, column = len(matrix), len(matrix[0])
        top, bottom, left, right = 0, row - 1, 0, column - 1
        res = []
        while top <= bottom and left <= right:
            for i in matrix[top][left: right + 1]:
                res.append(i)

            for j in matrix[top + 1: bottom + 1]:
                res.append(j[right])

            if top < bottom:
                for m in matrix[bottom][left: right][::-1]:
                    res.append(m)

            if left < right:
                for n in matrix[top + 1: bottom][::-1]:
                    res.append(n[left])

            top += 1
            right -= 1
            bottom -= 1
            left += 1

        return res


s = Solution()
# print s.printMatrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# print s.printMatrix([[1]])
print s.printMatrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])

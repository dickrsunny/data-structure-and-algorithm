#coding: utf-8

"""
有一个只由0，1，2三种元素构成的整数数组，请使用交换、原地排序而不是使用计数进行排序。

给定一个只含0，1，2的整数数组A及它的大小，请返回排序后的数组。保证数组大小小于等于500。

测试样例：
[0,1,1,0,2,2],6
返回：[0,0,1,1,2,2]

"""


class ThreeColor:
    def sortThreeColor(self, A, n):
        # write code here
        left, i = 0, 0
        right = n - 1
        while i <= right:
            if A[i] == 0:
                A[i], A[left] = A[left], A[i]
                left += 1
                i += 1
            elif A[i] == 2:
                A[i], A[right] = A[right], A[i]
                right -= 1
            else:
                i += 1
        return A


t = ThreeColor()
print t.sortThreeColor([0, 1, 2, 1, 0, 2, 0, 2, 1], 9)



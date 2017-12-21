# coding: utf-8

"""
数组中有一个数字出现的次数超过数组长度的一半，
请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0

"""


# -*- coding:utf-8 -*-
class Solution(object):

    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return 0

        length = len(numbers)
        if length == 1:
            return numbers[0]

        res = {}
        for i in numbers:
            if i in res:
                res[i] += 1
            else:
                res[i] = 1

        for key, val in res.iteritems():
            if val > length // 2:
                return key
        return 0

    # 最优解
    def MoreThanHalfNum_Solution2(self, numbers):
        if not numbers:
            return 0

        length = len(numbers)
        if length == 1:
            return numbers[0]

        num, count = numbers[0], 1
        for i in numbers:
            if i == num:
                count += 1
            else:
                count -= 1

            if count == 0:
                num = i
                count = 1

        count = 0
        for j in numbers:
            if j == num:
                count += 1

        if count > length // 2:
            return num
        return 0




s = Solution()
# print s.MoreThanHalfNum_Solution([1, 2, 3, 2, 4, 2, 5, 2, 3])
print s.MoreThanHalfNum_Solution2([1, 2, 3, 2, 4, 2, 5, 2, 3])

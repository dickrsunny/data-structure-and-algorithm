# coding: utf-8

"""
数组中有一个数字出现的次数超过数组长度的一半，
请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0

"""

"""
最优解解题思路：
如果有符合条件的数字，则它出现的次数比其他所有数字出现的次数和还要多。
在遍历数组时保存两个值：一是数组中一个数字，一是次数。遍历下一个数字时，
若它与之前保存的数字相同，则次数加1，否则次数减1；若次数为0，
则保存下一个数字，并将次数置为1。遍历结束后，所保存的数字即为所求。然后再判断它是否符合条件即可。


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

        num, count = numbers[0], 1
        for i in xrange(1, length):
            if count == 0:
                num = numbers[i]
                count = 1
            elif num == numbers[i]:
                count += 1
            else:
                count -= 1

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

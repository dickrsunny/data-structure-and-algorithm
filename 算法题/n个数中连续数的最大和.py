#coding: utf-8

'''
时间复杂度：O(N*lgN)
'''

class Solution:

    def __init__(self):
        self._max = 0

    def _sum(self, sub, left=True):
        if left:
            sub_length = len(sub)
            sum_ = max_ = sub[sub_length - 1]
            for i in range(len(sub)-2, -1, -1):
                sum_ += sub[i]
                if sum_ > max_:
                    max_ = sum_
        else:
            sum_ = max_ = sub[0]
            for j in range(1, len(sub)):
                sum_ += sub[j]
                if sum_ > max_:
                    max_ = sum_
        return max_

    def max_sum(self, array):
        if isinstance(array, list) and array:
            self._max = array[0]
            self.calculate(array)
            return self._max

    def calculate(self, array):
        length = len(array)
        if not array or length == 1:
            return

        half = length // 2
        left = array[:half]
        right = array[half:]
        self.calculate(left)
        self.calculate(right)

        max_left = self._sum(left)
        max_right = self._sum(right, False)
        if max_left > self._max:
            self._max = max_left
        if max_right > self._max:
            self._max = max_right

        if max_left + max_right > self._max:
            self._max = max_left + max_right


s = Solution()
print(s.max_sum([4, -3, 5, -2, -1, 2, 6, -2]))
print(s.max_sum([-3, -2, -1]))

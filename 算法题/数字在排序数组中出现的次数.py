# coding: utf-8

"""
统计一个数字在排序数组中出现的次数。

"""


class Solution(object):
    def GetNumberOfK(self, data, k):
        # write code here
        if not data or k < data[0]:
            return 0

        length = len(data)
        if length == 1:
            if k != data[0]:
                return 0
            else:
                return 1
        low = 0
        high = length - 1
        while low <= high:
            mid = (low + high) // 2
            if k < data[mid]:
                high = mid - 1
            elif k == data[mid]:
                break
            else:
                low = mid + 1
        if k == data[mid]:
            mid1 = mid2 = mid
            while mid1 >= 0 and data[mid1] == k:
                mid1 -= 1
            while mid2 < length and data[mid2] == k:
                mid2 += 1
            return mid2 - mid1 - 1
        return 0



s = Solution()
print s.GetNumberOfK([1, 2, 3, 3, 3, 3, 4, 5], 3)

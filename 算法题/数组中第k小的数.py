#coding: utf-8

"""
解题思路：

类快速排序算法：
随机选择一个元素作为枢纽元，然后将数组分为左右两部分，
根据左右两部分的大小来决定递归的区间，平均时间复杂度为O(N)，
但是最坏时间还是O(N^2)。这里跟快速排序有所不同，快速排序平均时间复杂度为O(NlgN)，
因为它需要递归调用两个部分，而寻找第K小的元素只需要考虑其中的一半

"""

class Solution(object):

    def find_kth_min(self, list_, k):
        if not list_:
            return

        length = len(list_)
        if 0 <= k < length:
            if length == 1:
                return list_[0]
            return self.sort(list_, 0, length - 1, k)

    def sort(self, list_, low, high, k):
        while low < high:
            j = self.partition(list_, low, high)
            if k == j:
                return list_[j]
            elif k > j:
                low = j + 1
            else:
                high = j - 1

        if low == high == k:
            return list_[low]

    def partition(self, list_, low, high):
        i, j = low, high + 1
        mid_val = list_[low]
        while True:
            while True:
                i += 1
                if list_[i] >= mid_val or i == high:
                    break
            while True:
                j -= 1
                if list_[j] <= mid_val:
                    break
            if i >= j:
                break
            list_[i], list_[j] = list_[j], list_[i]
        list_[low], list_[j] = list_[j], list_[low]
        return j


s = Solution()
print s.find_kth_min([1, 5], 1)




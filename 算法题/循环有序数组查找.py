# coding: utf-8

"""
https://leetcode.com/problems/search-in-rotated-sorted-array/
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""


class Solution:
    def binary_search(self, nums, low, high, target):
        while low <= high:
            mid = low + ((high - low) >> 1)
            if target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
            else:
                return mid

        return -1

    def search(self, nums, target):
        """
        自己实现的方式， 思路：
            每次切分总是会得到一个有序数组
            和一个循环数组；然后在有序数组
            中查找。
            若找到直接返回；否则循环数组继续执行上述过程

        """
        if not nums:
            return -1

        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + ((high - low) >> 1)
            if nums[low] <= nums[mid]:
                index = self.binary_search(nums, low, mid, target)
                if index != -1:
                    return index
                else:
                    low = mid + 1
            else:
                index = self.binary_search(nums, mid, high, target)
                if index != -1:
                    return index
                else:
                    high = mid - 1

        return -1

    ################################

    def search2(self, nums, target):
        """
        最优解
        """
        if not nums:
            return -1

        length = len(nums)
        low, high = 0, length - 1

        # find the index of the smallest value using binary search.
        # Loop will terminate since mid < hi,
        # and lo or hi will shrink by at least 1.
        # Proof by contradiction that mid < hi: if mid==hi,
        # then lo==hi and loop would have been terminated.
        while low < high:
            mid = low + ((high - low) >> 1)
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid

        # low==high is the index of the smallest value and also the number of places rotated.
        rot = low

        low, high = 0, length - 1
        while low <= high:
            mid = low + ((high - low) >> 1)
            real_mid = (mid + rot) % length
            if target > nums[real_mid]:
                low = mid + 1
            elif target < nums[real_mid]:
                high = mid - 1
            else:
                return real_mid

        return -1

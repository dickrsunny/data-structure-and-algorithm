#coding: utf-8

"""
https://leetcode.com/problems/kth-largest-element-in-an-array/
Find the kth largest element in an unsorted array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""

import heapq

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        h = nums[:k]
        heapq.heapify(h)
        for i in range(k, len(nums)):
            if nums[i] > h[0]:
                heapq.heappop(h)
                heapq.heappush(h, nums[i])

        return h[0]

    ###################################

    def partition(self, nums, low, high):
        i, j = low, high
        v = nums[low]
        while True:
            # 向右遍历，比v大或等于就退出循环
            while True:
                i += 1
                if v <= nums[i] or i == high:
                    break
            # 向左遍历，比v小或等于就退出循环
            while True:
                if v >= nums[j] or j == low:
                    break
                j -= 1

            if i >= j:
                break

            nums[i], nums[j] = nums[j], nums[i]

        nums[low], nums[j] = nums[j], nums[low]

        return j

    def sort(self, nums, low, high, k):
        if high <= low:
            return nums[low]

        j = self.partition(nums, low, high)
        if k < j:
            val = self.sort(nums, low, j - 1, k)
        elif k > j:
            val = self.sort(nums, j + 1, high, k)
        else:
            return nums[j]

        return val

    def findKthLargest2(self, nums, k):
        if not nums or k <= 0 or k > len(nums):
            return
        
        length = len(nums)

        if length == 1:
            return nums[0]

        k = length - k
        return self.sort(nums, 0, length - 1, k)

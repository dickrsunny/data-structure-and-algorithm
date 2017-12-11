# coding: utf-8

"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.

"""


class Solution(object):
    def findMin(self, nums):

        start, end = 0, len(nums) - 1

        while start < end:
            if nums[start] < nums[end]:
                return nums[start]
            else:
                mid = (start + end) // 2
                if nums[start] <= nums[mid]:
                    start = mid + 1
                else:
                    end = mid
        return nums[start]


s = Solution()
print s.findMin([4, 5, 6, 7, 0, 1, 2])

"""
time complexity: O(lgN)
space complexity: O(1)

"""

"""
Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.

"""


class Solution2(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums) - 1

        while start < end:
            if nums[start] < nums[end]:
                return nums[start]
            else:
                mid = (start + end) // 2
                if nums[start] < nums[mid]:
                    start = mid + 1
                elif nums[start] > nums[mid]:
                    end = mid
                else:
                    start += 1
        return nums[start]


s = Solution2()
print s.findMin([1, 0, 1, 1, 1])

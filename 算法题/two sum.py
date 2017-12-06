#coding: utf-8

"""
此算法时间复杂度为O(n),使用哈希表解决，
详细解释参考：https://leetcode.com/problems/two-sum/solution/
"""

"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for i in range(len(nums)):
            if target - nums[i] not in map:
                map[nums[i]] = i
            else:
                return map[target - nums[i]], i

        return -1, -1

s = Solution()
print s.twoSum([2, 7, 11, 15], 9)
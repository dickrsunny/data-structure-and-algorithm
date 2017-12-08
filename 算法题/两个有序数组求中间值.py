# coding: utf-8

"""


"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):

        i, j = 0, 0
        res = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
        res += nums1[i:]
        res += nums2[j:]

        length = len(res)
        half = length // 2
        if length % 2 == 1:
            return res[half]
        return (res[half - 1] + res[half]) / 2.0


s = Solution()
print s.findMedianSortedArrays([1, 3, 5], [2, 4, 6, 8])

"""
时间复杂度：O(n)
空间复杂度：O(n)

"""


class Solution2(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        length_A, length_B = len(nums1), len(nums2)
        if length_A > length_B:
            length_A, length_B, nums1, nums2 = length_B, length_A, nums2, nums1

        if length_B == 0:
            raise ValueError

        start, end, half = 0, length_A, (length_A + length_B + 1) // 2
        while start <= end:
            i = (start + end) // 2
            j = half - i
            if i < length_A and nums1[i] < nums2[j - 1]:
                start = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                end = end - 1
            else:
                if i == 0:
                    left = nums2[j - 1]
                elif j == 0:
                    left = nums1[i - 1]
                else:
                    left = max(nums1[i - 1], nums2[j - 1])

                if (length_A + length_B) % 2 == 1:
                    return left

                if i == length_A:
                    right = nums2[j]
                elif j == length_B:
                    right = nums1[i]
                else:
                    right = min(nums1[i], nums2[j])

                return (left + right) / 2.0


s = Solution2()
print s.findMedianSortedArrays([1, 3, 5], [2, 4, 6, 8])


"""
Complexity Analysis

Time complexity: O(log(min(m,n))).
At first, the searching range is [0, m]. And the length of this searching range will be reduced by half after each loop. 
So, we only need log(m) loops. 
Since we do constant operations in each loop, so the time complexity is O(log(m)). Since m≤n, so the time complexity is O(log(min(m,n))).

Space complexity: O(1).
We only need constant memory to store 9 local variables, so the space complexity is O(1).
详细解释请参考：https://leetcode.com/problems/median-of-two-sorted-arrays/solution/
"""
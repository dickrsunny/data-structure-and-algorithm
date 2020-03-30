
"""
Find the kth largest element in an unsorted array. Note that it is the kth 
largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""


class Solution:
    def findKthLargest(self, nums: list, k: int) -> int:
        if k > len(nums) or not nums:
            return -1

        return self.sort_(nums, 0, len(nums)-1, k)

    def partition(self, nums, low, high):
        i, j = low, high
        v = nums[low]
        while True:
            # 向右遍历，比v小就退出循环
            while True:
                i += 1
                if nums[i] < v or i == high:
                    break
            # 向左遍历，比v大就退出循环
            while True:
                if nums[j] > v or j == low:
                    break
                j -= 1

            if i >= j:
                break

            nums[i], nums[j] = nums[j], nums[i]

        nums[low], nums[j] = nums[j], nums[low]

        return j

    def sort_(self, nums, low, high, k):  # nums=[2, 1] low=0, high=1, k=2
        if low >= high:
            return nums[low]

        j = self.partition(nums, low, high)
        if k != j+1:
            if k > j+1:
                kth_val = self.sort_(nums, j+1, high, k)
            else:
                kth_val = self.sort_(nums, low, j-1, k)
            return kth_val

        return nums[j]

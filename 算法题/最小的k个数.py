# coding: utf-8

"""
输入n个整数，找出其中最小的K个数。
例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4

"""


class Solution(object):
    def min_heapify(self, root_pos, list_, length):
        left = 2 * root_pos + 1
        right = 2 * (root_pos + 1)
        pos = root_pos
        if left < length and list_[root_pos] > list_[left]:
            root_pos = left
        if right < length and list_[root_pos] > list_[right]:
            root_pos = right
        if root_pos != pos:
            list_[pos], list_[root_pos] = list_[root_pos], list_[pos]
            self.min_heapify(root_pos, list_, length)

    # 时间复杂度O(n + k*lgn)
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if not tinput or not k:
            return []

        length = len(tinput)
        if k > length:
            return []

        if length == 1:
            return tinput[0]

        # 建堆的时间复杂度为O(n)
        for i in range(length // 2 - 1, -1, -1):
            self.min_heapify(i, tinput, length)

        for i in range(length - 1, length - k - 1, -1):
            tinput[0], tinput[i] = tinput[i], tinput[0]
            self.min_heapify(0, tinput, i)
        return tinput[-k:]


    def max_heapify(self, root_pos, list_, length):
        left = 2 * root_pos + 1
        right = 2 * (root_pos + 1)
        pos = root_pos
        if left < length and list_[root_pos] < list_[left]:
            root_pos = left
        if right < length and list_[root_pos] < list_[right]:
            root_pos = right
        if root_pos != pos:
            list_[pos], list_[root_pos] = list_[root_pos], list_[pos]
            self.max_heapify(root_pos, list_, length)

    """
    时间复杂度：n*lgk （最优解）
    
    该算法非常适合海量数据处理，尤其在内存有限，
    不能一次读入所有的数据时，当n很大，而k较小时，
    一次向内存读入k个数据，而后每次可以读入一个进行比较，
    这对于内存最多可容纳k个数据时便可满足要求
    """
    def GetLeastNumbers_Solution2(self, tinput, k):
        if not tinput or not k:
            return []

        length = len(tinput)
        if k > length:
            return []

        temp = tinput[:k]
        for i in (range(k // 2 - 1, -1, -1)):
            self.max_heapify(i, temp, k)

        for j in tinput[k:]:
            if j < temp[0]:
                temp[0] = j
                self.max_heapify(0, temp, k)

        # 这一步是堆排序，可去掉
        for m in range(k - 1, 0, -1):
            temp[0], temp[m] = temp[m], temp[0]
            self.max_heapify(0, temp, m)

        return temp

s = Solution()
# print s.GetLeastNumbers_Solution([4, 5, 1, 6, 2, 7, 3, 8], 4)
# print s.GetLeastNumbers_Solution([4, 3, 5, 6, 2], 4)
# print s.GetLeastNumbers_Solution2([4, 5, 1, 6, 2, 7, 3, 8], 4)
print s.GetLeastNumbers_Solution2([4, 3, 5, 6, 2], 4)


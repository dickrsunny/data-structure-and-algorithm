# coding:utf-8
from __future__ import division

"""
有一个整形数组A，请设计一个复杂度为O(n)的算法，算出排序后相邻两数的最大差值。
"""


class Gap:
    def maxGap(self, A, n):
        # write code here
        max_val, min_val = max(A), min(A)
        gap = (max_val - min_val) / n
        sorted_list = [[] for _ in range(n + 1)]
        for i in A:
            sorted_list[int((i - min_val) // gap)].append(i)
        print(sorted_list)
        max_gap = -1
        for k in range(1, len(sorted_list) - 1):
            if not sorted_list[k]:
                l = k - 1
                while not sorted_list[l]:
                    l -= 1
                left_list = sorted_list[l]
                r = k + 1
                while not sorted_list[r]:
                    r += 1
                right_list = sorted_list[r]
                res = min(right_list) - max(left_list)
                if res > max_gap:
                    max_gap = res
        return max_gap


g = Gap()
print g.maxGap([7778, 9763, 347, 8793, 4297], 5)

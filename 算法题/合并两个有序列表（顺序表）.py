#coding: utf-8

"""
时间复杂度：O(n + m)
空间复杂度：O(1)

"""

class Solution(object):

    def merge_two_sort(self, l1, l2):
        # res = []
        # i, j = 0, 0
        # while i < len(l1) and j < len(l2):
        #     if l1[i] <= l2[j]:
        #         res.append(l1[i])
        #         i += 1
        #     else:
        #         res.append(l2[j])
        #         j += 1
        # res.extend(l1[i:])
        # res.extend(l2[j:])
        # return res

        length1, length2 = len(l1), len(l2)
        total_length = length1 + length2 - 1
        i, j = length1 - 1, length2 - 1
        l1.extend(l2)
        while i >= 0 and j >= 0:
            if l1[i] >= l2[j]:
                l1[total_length] = l1[i]
                i -= 1
            else:
                l1[total_length] = l2[j]
                j -= 1
            total_length -= 1

        # print l1, i, j, total_length
        while j >= 0:
            l1[total_length] = l2[j]
            j -= 1
            total_length -= 1
        return l1

    def merge_two_sort_recursively(self, l1, l2, i, j, res):
        if i == len(l1) or j == len(l2):
            res.extend(l1[i:])
            res.extend(l2[j:])
            return

        if l1[i] <= l2[j]:
            res.append(l1[i])
            self.merge_two_sort_recursively(l1, l2, i + 1, j, res)
        else:
            res.append(l2[j])
            self.merge_two_sort_recursively(l1, l2, i, j + 1, res)
        return res




s = Solution()
print s.merge_two_sort([1, 3, 5], [2, 4, 6])
# print s.merge_two_sort_recursively([1, 3, 5], [2, 4, 6], 0, 0, [])
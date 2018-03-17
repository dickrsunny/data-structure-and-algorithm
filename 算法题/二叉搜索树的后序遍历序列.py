# coding: utf-8

"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。
假设输入的数组的任意两个数字都互不相同。

"""


class Solution(object):
    def VerifySequenceOfBST(self, sequence):
        # write code here
        length = len(sequence)
        if length == 0:
            return False
        if length == 1:
            return True

        root = sequence[-1]
        i = 0
        while sequence[i] < root:
            i += 1

        for item in sequence[i: length - 1]:
            if item < root:
                return False

        left = True
        if i > 0:
            left = self.VerifySequenceOfBST(sequence[:i])

        right = True
        if i < length - 1:
            right = self.VerifySequenceOfBST(sequence[i: length - 1])

        return left and right


    def VerifySequenceOfBST2(self, sequence):
        if not sequence:
            return False

        return self.detail_do(sequence, 0, len(sequence) - 1)


    def detail_do(self, sequence, low, high):
        if low >= high:
            return True

        i = low
        while i < high and sequence[i] < sequence[high]:
            i += 1

        j = i
        while j < high:
            if sequence[j] < sequence[high]:
                return False
            j += 1

        return self.detail_do(sequence, low, i - 1) and self.detail_do(sequence, i, high - 1)


s = Solution()
# print s.VerifySequenceOfBST([1, 4, 7, 6, 3, 13, 14, 10, 8])
# print s.VerifySequenceOfBST([2, 1, 3, 4, 1])
print s.VerifySequenceOfBST([1, 3, 2])

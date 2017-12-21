# coding: utf-8

"""
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c
所能排列出来的所有字符串abc,acb,bac,bca,cab和cba

"""


class Solution(object):
    def Permutation(self, ss):
        # write code here
        if not len(ss):
            return []
        if len(ss) == 1:
            return list(ss)

        charList = list(ss)
        charList.sort()
        pStr = []
        for i in range(len(charList)):
            if i > 0 and charList[i] == charList[i - 1]:  # 重复元素跳过
                continue
            temp = self.Permutation(ss[:i] + ss[i + 1:])  # 除去取出的元素，剩余元素递归全排列
            for j in temp:
                pStr.append(charList[i] + j)
        return pStr


s = Solution()
print s.Permutation('aab')

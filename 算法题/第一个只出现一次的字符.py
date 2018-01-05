#coding: utf-8

"""
在一个字符串(1<=字符串长度<=10000，全部由字母组成)
中找到第一个只出现一次的字符,并返回它的位置

"""


from collections import OrderedDict


class Solution(object):
    def FirstNotRepeatingChar(self, s):
        # write code here
        if not s:
            return -1

        length = len(s)
        if length == 1:
            return 0
        for i in range(length):
            elem = s[i]
            left = s[:i] + s[i + 1:]
            if elem not in left:
                return i

    def FirstNotRepeatingChar2(self, s):
        if not s:
            return -1

        length = len(s)
        if length == 1:
            return 0
        res = OrderedDict()
        for i in s:
            if i not in res:
                res[i] = 1
            else:
                res[i] += 1

        for key,value in res.iteritems():
            if value == 1:
                return s.index(key)



s = Solution()
print s.FirstNotRepeatingChar2('google')
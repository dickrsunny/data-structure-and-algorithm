#coding: utf-8

"""
题目描述
请实现一个函数，将一个字符串中的空格替换成“%20”。
例如，当字符串为We Are Happy，
则经过替换之后的字符串为We%20Are%20Happy

"""

class Solution:
    def replaceSpace(self, s):
        str_ = ''
        for i in s:
            if i == ' ':
                i = '%20'
            str_ += i
        return str_


s = Solution()
print s.replaceSpace('w e')
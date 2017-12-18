#coding: utf-8

"""
求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？
为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,
但是对于后面问题他就没辙了。ACMer希望你们帮帮他,并把问题更加普遍化,
可以很快的求出任意非负整数区间中1出现的次数。

"""

"""
详细解释请参考：https://discuss.leetcode.com/topic/18054/4-lines-o-log-n-c-java-python

"""

class Solution(object):
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        ones = 0
        m = r = 1
        while n > 0:
            ones += (n + 8) / 10 * m + (n % 10 == 1) * r
            r += n % 10 * m
            m *= 10
            n /= 10
        return ones


s = Solution()
print s.NumberOf1Between1AndN_Solution(100)
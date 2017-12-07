# coding: utf-8

"""
Complexity Analysis

Time complexity : O(n). Index j will iterate n times.

Space complexity : O(m). m is the size of the dict.
详细解释参考：https://leetcode.com/problems/longest-substring-without-repeating-characters/solution/

"""



class Solution(object):
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        max_length = left = 0
        accessed_char = {}
        for right in range(len(s)):
            # 检查当前字符是否在访问的字典中，如果在，更新滑动窗口的左边沿为上一个当前字符的下一个位置
            if s[right] in accessed_char:
                left = max(accessed_char[s[right]], left)

            # 每遍历一个字符，都要计算一次最大长度并和上一次的长度比较，取较大的长度
            max_length = max(max_length, right - left + 1)
            accessed_char[s[right]] = right + 1
        return max_length

s = Solution()
print s.lengthOfLongestSubstring('pwwkew')
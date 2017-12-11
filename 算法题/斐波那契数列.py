#coding: utf-8

"""
要求输入一个整数n，
请你输出斐波那契数列的第n项

"""

class Solution(object):
    def Fibonacci(self, n):
        # write code here
        i = 0
        j = 1
        for m in range(n):
            i, j = j, i + j
        return i
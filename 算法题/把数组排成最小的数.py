# coding: utf-8

"""
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，
打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，
则打印出这三个数字能排成的最小数字为321323。

"""


class Solution(object):
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ''

        length = len(numbers)
        if length == 1:
            return numbers[0]

        numbers = map(str, numbers)
        for i in range(0, length):
            for j in range(i, length):
                if (numbers[i] + numbers[j]) > (numbers[j] + numbers[i]):
                    tmp = numbers[i]
                    numbers[i] = numbers[j]
                    numbers[j] = tmp
        return int(''.join(numbers))


s = Solution()
print s.PrintMinNumber([3, 32, 321])

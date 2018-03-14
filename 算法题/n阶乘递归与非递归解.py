#coding: utf-8


class Solution:
    def n_factorial(self, n):
        if n <= 1:
            return n
        return n * self.n_factorial(n - 1)

    def n_factorial_non_recursively(self, n):
        if n <= 1:
            return n
        res = 1
        while n > 1:
            res = res * n
            n = n - 1
        return res



s = Solution()
print(s.n_factorial(6))
print(s.n_factorial_non_recursively(6))
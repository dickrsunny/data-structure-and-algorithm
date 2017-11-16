class Subsequence:
    def shortestSubsequence(self, A, n):
        # write code here
        _max = A[0]
        max_site = 0
        for i in range(1, n):
            if _max > A[i]:
                max_site = i
            else:
                _max = A[i]

        _min = A[n - 1]
        min_site = 0
        for j in range(n - 2, -1, -1):
            if _min < A[j]:
                min_site = j
            else:
                _min = A[i]
        if max_site == 0 and min_site == 0:
            return 0
        else:
            return max_site - min_site + 1


s = Subsequence()
print s.shortestSubsequence([1, 2, 3, 3, 8, 9], 6)

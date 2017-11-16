class Merge:
    def mergeAB(self, A, B, n, m):
        # write code here
        res = [0 for _ in range(n + m)]
        entity = n + m - 1
        i = n - 1
        j = m - 1
        while i >= 0 and j >= 0:
            if A[i] >= B[j]:
                res[entity] = A[i]
                i -= 1
            else:
                res[entity] = B[j]
                j -= 1
            entity -= 1
        if i >= 0:
            for m in range(i+1):
                res[m] = A[m]
        if j >= 0:
            for n in range(j+1):
                res[n] = B[n]
        return res


m = Merge()
print m.mergeAB([1, 3, 5, 7, 9], [2, 4, 6, 8], 5, 4)
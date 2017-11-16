class CountingSort:
    def countingSort(self, A, n):
        # write code here
        _max, _min = max(A), min(A)
        site = [0] * (_max - _min + 1)
        sorted_A = [0 for _ in range(n)]
        for i in A:
            site[i - _min] += 1
        k = 0
        for j in range(_max - _min + 1):
            for _ in range(site[j]):
                sorted_A[k] = j + _min
                k += 1
        return sorted_A


c = CountingSort()
print c.countingSort([1, 2, 3, 5, 2, 3], 6)

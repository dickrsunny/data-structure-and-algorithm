def radixSort(A, n):
    for i in range(4):
        s = [[] for _ in range(10)]
        for j in A:
            s[j // (10 ** i) % 10].append(j)
        A = [a for b in s for a in b]
    return A


print(radixSort([1, 2, 3, 5, 2, 3], 6))

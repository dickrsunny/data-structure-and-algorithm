def shellSort(A, n):
    gap = int(round(n / 2))
    while gap > 0:
        for i in range(gap, n):
            if A[i - gap] > A[i]:
                tmp = A[i]
                A[i] = A[i - gap]
                A[i - gap] = tmp
        gap -= 1
    return A


print shellSort([1, 2, 7, 5, 2, 9, 3], 7)

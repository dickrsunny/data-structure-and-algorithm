#coding: utf-8

def shellSort(A, n):
    h = 1
    while h < n // 3:
        h = 3 * h + 1

    while h >= 1:
        for i in xrange(1, n):
            j = i
            while j >=h and A[j - h] > A[j]:
                A[j - h], A[j] = A[j], A[j - h]
                j -= h
        h //= 3
    return A



print shellSort([1, 2, 7, 5, 2, 9, 3], 7)

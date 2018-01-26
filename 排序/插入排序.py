#coding: utf-8

def insertSort(A, n):
    if not A or n == 1:
        return A

    for i in range(1, n):
        temp = A[i]
        j = i
        while j > 0 and temp < A[j - 1]:
            A[j] = A[j - 1]
            j -= 1
        A[j] = temp
    return A

print insertSort([1, 2, 7, 5, 2, 9, 3], 7)

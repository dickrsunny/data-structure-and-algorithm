#coding: utf-8
def insertSort(A, n):
    # write code here
    for i in range(1, n):
        for j in range(0, i):
            if A[i] < A[j]:
                temp = A[i]
                A[i] = A[j]
                A[j] = temp
    return A

print insertSort([1, 2, 7, 5, 2, 9, 3], 7)

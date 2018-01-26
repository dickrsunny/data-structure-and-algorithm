#coding: utf-8
def insertSort(A, n):
    # write code here
    if not A or n == 1:
        return A

    for i in range(1, n):
        for j in range(i):
            if A[i] < A[j]:
                temp = A[i]
                A[i] = A[j]
                A[j] = temp
    return A

print insertSort([1, 2, 7, 5, 2, 9, 3], 7)

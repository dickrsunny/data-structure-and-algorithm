#coding: utf-8

def insertSort(A, n):
    if not A or n == 1:
        return A

    # 比较当前数和前一个数的大小，如果前一个数大于当前数，就交换位置
    for i in xrange(1, n):
        j = i
        while j > 0 and A[j] < A[j - 1]:
            A[j], A[j - 1] = A[j - 1], A[j]
            j -= 1
    return A

print insertSort([1, 2, 7, 5, 2, 9, 3], 7)

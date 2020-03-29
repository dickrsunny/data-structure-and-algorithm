
def insertSort(a, n):
    if not a or n == 1:
        return a

    # 从第二个数开始比较当前数和前一个数的大小，
    # 如果前一个数大于当前数，就将前面的数向后挪，
    # 找到位置之后，直接插入。
    for i in range(1, n):
        val = a[i]
        j = i
        while j > 0 and a[j-1] > val:
            a[j] = a[j-1]
            j -= 1

        a[j] = val
    return a


print(insertSort([1, 2, 7, 5, 2, 9, 3], 7))

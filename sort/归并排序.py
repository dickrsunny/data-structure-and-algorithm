#coding:utf-8
def mergeSort(seq):
    if len(seq) == 1:
        return seq
    else:
        middle = len(seq) // 2
        left = mergeSort(seq[:middle])
        right = mergeSort(seq[middle:])

        i = 0  # left 计数
        j = 0  # right 计数
        k = 0  # 总计数

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                seq[k] = left[i]
                i += 1
                k += 1
            else:
                seq[k] = right[j]
                j += 1
                k += 1

        remain = left if i < j else right
        r = i if remain == left else j

        while r < len(remain):
            seq[k] = remain[r]
            r += 1
            k += 1

        return seq


print mergeSort([1, 2, 7, 5, 2, 9, 3])

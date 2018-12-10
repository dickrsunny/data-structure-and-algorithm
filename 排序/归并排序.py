# coding:utf-8


def mergeSort(seq):
    if not seq or len(seq) <= 1:
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
            else:
                seq[k] = right[j]
                j += 1
            k += 1

        if i < j:
            remain = left
            r = i
        else:
            remain = right
            r = j

        length = len(remain)
        while r < length:
            seq[k] = remain[r]
            r += 1
            k += 1

        return seq


def mergeSort2(seq, left, right):
    if left >= right:
        return seq[left: right + 1]
    else:
        middle = (right + left + 1) // 2
        left = mergeSort2(seq, left, middle - 1)
        right = mergeSort2(seq, middle, right)

        i = 0  # left 计数
        j = 0  # right 计数

        temp = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                temp.append(left[i])
                i += 1
            else:
                temp.append(right[j])
                j += 1

        temp.extend(left[i:])
        temp.extend(right[j:])

        return temp


print(mergeSort([1, 2, 7, 5, 2, 9, 3]))

def bubbleSort(alist):
    if not alist or len(alist) == 1:
        return alist

    length = len(alist)
    for passnum in range(length - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp
    return alist


print(bubbleSort([1, 2, 7, 5, 2, 9, 3]))

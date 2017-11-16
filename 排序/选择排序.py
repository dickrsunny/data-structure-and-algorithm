def selectionSort(alist):
    for i in range(len(alist) - 1, 0, -1):
        maxone = 0
        for j in range(1, i + 1):
            if alist[j] > alist[maxone]:
                maxone = j
        temp = alist[i]
        alist[i] = alist[maxone]
        alist[maxone] = temp
    return alist

print(selectionSort([1, 2, 7, 5, 2, 9, 3]))

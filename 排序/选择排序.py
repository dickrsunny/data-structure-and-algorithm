#coding: utf-8


def selectionSort(alist):
    if not alist or len(alist) == 1:
        return

    for i in range(len(alist) - 1, 0, -1):
        maxone = 0
        # 每次找到剩余列表中的最大值
        for j in range(1, i + 1):
            if alist[j] > alist[maxone]:
                maxone = j
        temp = alist[i]
        alist[i] = alist[maxone]
        alist[maxone] = temp
    return alist

print(selectionSort([10, 2, 7, 5, 2, 9, 3]))

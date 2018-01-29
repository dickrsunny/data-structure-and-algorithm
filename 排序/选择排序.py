#coding: utf-8


def selectionSort(alist):
    if not alist or len(alist) == 1:
        return

    length = len(alist)
    # 依次遍历数组中的元素，在剩余的元素中找比自己小的元素，若找到，则交换值，否则和自身交换
    for i in xrange(length):
        min_site = i
        for j in xrange(i + 1, length):
            if alist[j] < alist[min_site]:
                min_site = j
        alist[i], alist[min_site] = alist[min_site], alist[i]
    return alist


print(selectionSort([10, 2, 7, 5, 2, 9, 3]))


def selectionSort(a):
    if not a or len(a) == 1:
        return

    length = len(a)
    # 依次遍历数组中的元素，在剩余的元素中找比自己小的元素，若找到，则交换值，否则和自身交换
    for i in range(length - 1):
        min_site = i
        for j in range(i + 1, length):
            if a[min_site] > a[j]:
                min_site = j
        a[i], a[min_site] = a[min_site], a[i]

    return a


print(selectionSort([10, 2, 7, 5, 2, 9, 3]))

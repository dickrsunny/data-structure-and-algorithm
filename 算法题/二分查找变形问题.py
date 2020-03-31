# coding: utf-8


# 变体一：查找第一个值等于给定值的元素（变体三的特殊情况）

def bsearch(a, n, value):
    if not a:
        return -1

    low = 0
    high = n - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if a[mid] >= value:
            high = mid - 1
        else:
            low = mid + 1

    if low < n and a[low] == value:
        return low
    else:
        return -1


# 变体二：查找最后一个值等于给定值的元素（变体四的特殊情况）

def bsearch2(a, n, value):
    if not a:
        return -1

    low = 0
    high = n - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if a[mid] > value:
            high = mid - 1
        else:
            low = mid + 1

    if a[low - 1] == value:
        return low - 1
    else:
        return -1


# 变体三：查找第一个值大于等于给定值的元素

def bsearch3(a, n, value):
    if not a:
        return -1

    low = 0
    high = n - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if a[mid] >= value:
            high = mid - 1
        else:
            low = mid + 1

    if low < n:
        return low
    else:
        return -1


# 变体四：查找最后一个值小于等于给定值的元素

def bsearch4(a, n, value):
    if not a:
        return -1

    low = 0
    high = n - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if a[mid] > value:
            high = mid - 1
        else:
            low = mid + 1

    if a[low - 1] <= value:
        return low - 1
    else:
        return -1


print(bsearch4([3, 5, 6, 8, 9, 10], 6, 7))

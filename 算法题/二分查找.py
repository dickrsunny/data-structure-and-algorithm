#coding: utf-8

"""
最坏时间复杂度	O(log n)
最优时间复杂度	O(1)
平均时间复杂度	O(log n)
空间复杂度 迭代： O(1)  递归： O(log n)

"""

def binary_search(list_, elem):
    length = len(list_)
    left, right = 0, length - 1
    while left <= right:
        mid = (left + right) // 2
        if elem == list_[mid]:
            return mid
        elif elem > list_[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return 'not found'


def binary_search_recursively(list_, elem, left, right):
    if left > right:
        return 'not found'

    mid = (left + right) // 2
    if elem == list_[mid]:
        return mid
    elif elem > list_[mid]:
        return binary_search_recursively(list_, elem, mid + 1, right)
    else:
        return binary_search_recursively(list_, elem, left, mid - 1)


# print binary_search([1, 3, 4, 6, 7, 8, 10, 13, 14], 6)
print binary_search_recursively([1, 3, 4, 6, 7, 8, 10, 13, 14], 6, 0, 8)


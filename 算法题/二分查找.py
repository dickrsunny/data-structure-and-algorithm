
"""
最坏时间复杂度	O(log n)
最优时间复杂度	O(1)
平均时间复杂度	O(log n)
空间复杂度 迭代： O(1)  递归： O(log n)

"""


def binary_search(list_, elem):
    length = len(list_)
    low, high = 0, length - 1

    while low <= high:
        mid = low + (high - low) // 2
        if elem == list_[mid]:
            return mid
        elif elem > list_[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def binary_search_recursively(list_, elem, low, high):
    if low > high:
        return -1

    mid = low + (high - low) // 2
    if elem == list_[mid]:
        return mid
    elif elem > list_[mid]:
        return binary_search_recursively(list_, elem, mid + 1, high)
    else:
        return binary_search_recursively(list_, elem, low, mid - 1)


print(binary_search([1, 3, 4, 6, 7, 8, 10, 13, 14], 6))
# print(binary_search_recursively([1, 3, 4, 6, 7, 8, 10, 13, 14], 6, 0, 8))

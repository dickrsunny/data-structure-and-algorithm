#coding: utf-8

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

print binary_search([1, 2, 3, 4, 5, 6, 9], 7)


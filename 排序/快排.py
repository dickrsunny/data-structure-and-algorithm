def quicksort(_list):
    if not _list:
        return []
    first_ele = _list[0]
    lesser_to_ele = quicksort([item for item in _list[1:] if item <= first_ele])
    bigger_to_ele = quicksort([item for item in _list[1:] if item > first_ele])
    return lesser_to_ele + [first_ele] + bigger_to_ele


print(quicksort([1, 2, 3, 5, 2, 3]))

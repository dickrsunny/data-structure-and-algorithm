def bubbleSort(l):
    if not l or len(l) == 1:
        return l

    length = len(l)
    for i in range(length):
        j = 0
        while (j < length - i - 1):
            if l[j] > l[j+1]:
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp
            j += 1

    return l


print(bubbleSort([1, 2, 7, 5, 2, 9, 3]))

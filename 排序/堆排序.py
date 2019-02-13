"""
class HeapSort:
    def heapSort(self, A, n):
        if A is not None and n >= 2:
            self.buildMaxHeap(A, n)
            # print(A)
            for i in range(n - 1, 0, -1):
                A[0], A[i] = A[i], A[0]
                self.maxHeapify(A, i, 0)
        return A

    # write code here

    def buildMaxHeap(self, arr, heap_size):
        if heap_size < 2:
            return
        last_branch_node = heap_size // 2 - 1

        for i in range(last_branch_node, -1, -1):
            self.maxHeapify(arr, heap_size, i)
            print arr

    def maxHeapify(self, arr, heap_size, root_pos):
        left_child = 2 * root_pos + 1
        right_child = 2 * (root_pos + 1)
        max_value_pos = root_pos

        if left_child < heap_size and arr[left_child] > arr[max_value_pos]:
            max_value_pos = left_child
        if right_child < heap_size and arr[right_child] > arr[max_value_pos]:
            max_value_pos = right_child
        if max_value_pos != root_pos:
            arr[root_pos], arr[max_value_pos] = arr[max_value_pos], arr[root_pos]
            self.maxHeapify(arr, heap_size, max_value_pos)


h = HeapSort()
print h.heapSort([1, 2, 7, 5, 2, 9, 3], 7)
"""


class HeapSort(object):

    def sort(self, list_):
        if not list_ or len(list_) == 1:
            return list_

        self.heapify(list_)
        length = len(list_) - 1
        for i in range(length, 0, -1):
            list_[0], list_[i] = list_[i], list_[0]
            self.sift_down(list_, 0, i)
        return list_

    def heapify(self, list_):
        length = len(list_)
        half = length // 2 - 1
        for i in range(half, -1, -1):
            self.sift_down(list_, i, length)

    def sift_down(self, list_, root_pos, length):
        while root_pos * 2 + 1 < length:
            left_pos = root_pos * 2 + 1
            right_pos = root_pos * 2 + 2
            if right_pos < length and list_[left_pos] < list_[right_pos]:
                left_pos = right_pos

            if list_[root_pos] < list_[left_pos]:
                list_[root_pos], list_[left_pos] = list_[left_pos], list_[root_pos]
            else:
                break

            root_pos = left_pos


h = HeapSort()
print(h.sort([6, 5, 7, 2, 9, 3]))

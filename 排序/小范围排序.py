class HeapSort:
    def heapSort(self, A, n, k):
        if A is not None and n >= 2:
            heap = A[:k]
            self.buildMaxHeap(heap, k)
            print A, heap
            for i in range(k, n):
                A[i - k] = heap[0]
                heap[0] = A[i]
                self.maxHeapify(heap, k, 0)
            print A, heap
            for j in range(n - k, n):
                A[n - k], heap[0] = heap[0], heap[k - 1]
                k -= 1
                self.maxHeapify(heap, k, 0)
        return A

    # write code here

    def buildMaxHeap(self, arr, heap_size):
        if heap_size < 2:
            return
        last_branch_node = heap_size // 2 - 1

        for i in range(last_branch_node, -1, -1):
            self.maxHeapify(arr, heap_size, i)

    def maxHeapify(self, arr, heap_size, root_pos):
        # print(arr, heap_size)
        left_child = 2 * root_pos + 1
        right_child = 2 * (root_pos + 1)
        max_value_pos = root_pos

        if left_child < heap_size and arr[left_child] < arr[max_value_pos]:
            max_value_pos = left_child
        if right_child < heap_size and arr[right_child] < arr[max_value_pos]:
            max_value_pos = right_child
        if max_value_pos != root_pos:
            arr[root_pos], arr[max_value_pos] = arr[max_value_pos], arr[root_pos]
            self.maxHeapify(arr, heap_size, max_value_pos)


h = HeapSort()
print h.heapSort([3, 2, 1, 6, 5, 4, 9, 8, 7, 10], 10, 3)

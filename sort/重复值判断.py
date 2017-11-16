class Checker:
    def checkDuplicate(self, A, n):
        # write code here
        if A is not None and n >= 2:
            self.buildMaxHeap(A, n)
            for i in range(n - 1, 0, -1):
                A[0], A[i] = A[i], A[0]
                self.maxHeapify(A, i, 0)
                if A[0] == A[i]:
                    return True
            return False


    def buildMaxHeap(self, arr, heap_size):
        if heap_size < 2:
            return
        last_branch_node = heap_size // 2 - 1

        for i in range(last_branch_node, -1, -1):
            self.maxHeapify(arr, heap_size, i)


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


c = Checker()
print(c.checkDuplicate([1, 2, 7, 5, 2, 9, 3], 7))
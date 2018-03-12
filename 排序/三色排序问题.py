class ThreeColor:
    def sortThreeColor(self, A, n):
        # write code here
        left, i = 0, 0
        right = n - 1
        while i <= right:
            if A[i] == 0:
                A[i], A[left] = A[left], A[i]
                left += 1
                i += 1
            elif A[i] == 2:
                A[i], A[right] = A[right], A[i]
                right -= 1
            else:
                i += 1
        return A


t = ThreeColor()
print t.sortThreeColor([0, 1, 2, 1, 0, 2, 0, 2, 1], 9)



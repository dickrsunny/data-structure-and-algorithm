class ThreeColor:
    def sortThreeColor(self, A, n):
        # write code here
        i = 0
        j = n - 1
        k = 0
        while i <= j:
            if A[i] == 0:
                A[i], A[k] = A[k], A[i]
                i += 1
                k += 1
            elif A[i] == 2:
                A[i], A[j] = A[j], A[i]
                j -= 1
            else:
                i += 1
        return A


t = ThreeColor()
print t.sortThreeColor([0, 1, 2, 1, 0, 2, 0, 2, 1], 9)



class Finder:
    def findX(self, mat, n, m, x):
        # write code here
        i = 0  #
        j = m - 1

        while i < n and j >= 0:
            if mat[i][j] == x:
                return True
            elif mat[i][j] < x:
                i += 1
            else:
                j -= 1
        return False


f = Finder()
print(f.findX([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, 3, 10))

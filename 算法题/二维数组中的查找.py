
class Solution(object):
    def Find(self, target, array):
        # write code here
        column, row = len(array), len(array[0])
        i, j = 0, row - 1
        while i < column and j >= 0:
            if target == array[i][j]:
                return True
            elif target > array[i][j]:
                i += 1
            else:
                j -= 1
        return False

s = Solution()
print s.Find(6, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

class Solution(object):

    def list_reverse(self, list_):

        length = len(list_)
        i, j = 0, length - 1
        while i < j:
            list_[i], list_[j] = list_[j], list_[i]
            i += 1
            j -= 1
        return list_

s = Solution()
print s.list_reverse([1, 2, 3, 4, 5, 6, 7])

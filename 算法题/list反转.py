
class Solution(object):

    def list_reverse(self, list_):

        length = len(list_)
        i, j = 0, length - 1
        while i < j:
            list_[i], list_[j] = list_[j], list_[i]
            i += 1
            j -= 1
        return list_

    def list_reverse2(self, list_):
        half = len(list_) // 2
        if half != 0:
            for i in xrange(half):
                list_[i], list_[-(i + 1)] = list_[-(i + 1)], list_[i]
        return list_



s = Solution()
print s.list_reverse2([1, 2, 3, 4, 5, 6, 7, 8])

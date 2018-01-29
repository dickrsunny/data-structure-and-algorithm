#coding: utf-8

class Solution(object):

    def partition(self, _list, low, high):
        i, j = low, high + 1
        v = _list[low]
        while True:
            # 向右遍历，比v大就退出循环
            while True:
                i += 1
                if v <= _list[i] or i == high:
                    break
            # 向左遍历，比v小就退出循环
            while True:
                j -= 1
                if v >= _list[j]:
                    break

            if i >= j:
                break

            _list[i], _list[j] = _list[j], _list[i]

        _list[low], _list[j] = _list[j], _list[low]
        return j

    def sort(self, _list, low, high):
        if high <= low:
            return

        j = self.partition(_list, low, high)
        self.sort(_list, low, j - 1)
        self.sort(_list, j + 1, high)

    # 普通无大量重复元素
    def quick_sort(self, _list):
        if not _list or len(_list) == 1:
            return

        self.sort(_list, 0, len(_list) - 1)
        return _list


    def sort2(self, _list, low, high):
        if high <= low:
            return

        lt, i, gt = low, low + 1, high
        v = _list[low]
        while i <= gt:
            if _list[i] < v:
                _list[i], _list[lt] = _list[lt], _list[i]
                i += 1
                lt += 1

            elif _list[i] > v:
                _list[i], _list[gt] = _list[gt], _list[i]
                gt -= 1

            else:
                i += 1
        self.sort2(_list, low, lt - 1)
        self.sort2(_list, gt + 1, high)


    # 大量重复元素
    def quick_sort2(self, _list):
        if not _list or len(_list) == 1:
            return

        self.sort2(_list, 0, len(_list) - 1)
        return _list



s = Solution()
print s.quick_sort([1, 2, 1, 3, 5, 2, 3])
# print s.quick_sort2([1, 2, 1, 3, 5, 2, 3])

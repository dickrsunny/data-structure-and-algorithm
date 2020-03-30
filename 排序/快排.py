
class Solution:
    def partition(self, a, low, high):
        i, j = low, high
        v = a[low]
        while True:
            # 向右遍历，比v大就退出循环
            while True:
                i += 1
                if a[i] > v or i == high:
                    break
            # 向左遍历，比v小就退出循环
            while True:
                if a[j] < v or j == low:
                    break
                j -= 1

            if i >= j:
                break

            a[i], a[j] = a[j], a[i]

        a[low], a[j] = a[j], a[low]

        return j

    def sort(self, a, low, high):
        if low >= high:
            return

        j = self.partition(a, low, high)
        self.sort(a, low, j - 1)
        self.sort(a, j + 1, high)

    # 普通无大量重复元素
    def quick_sort(self, a):
        self.sort(a, 0, len(a) - 1)
        return a

    ####################################

    def sort2(self, a, low, high):
        if high <= low:
            return

        lt, i, gt = low, low + 1, high
        v = a[low]
        while i <= gt:
            if a[i] < v:
                a[i], a[lt] = a[lt], a[i]
                i += 1
                lt += 1

            elif a[i] > v:
                a[i], a[gt] = a[gt], a[i]
                gt -= 1

            else:
                i += 1
        self.sort2(a, low, lt - 1)
        self.sort2(a, gt + 1, high)

    # 大量重复元素
    def quick_sort2(self, a):
        self.sort2(a, 0, len(a) - 1)
        return a


s = Solution()
print(s.quick_sort([1, 2, 1, 3, 5, 2, 3]))
# print s.quick_sort2([1, 2, 1, 3, 5, 2, 3])

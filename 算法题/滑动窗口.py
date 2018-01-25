# coding: utf-8

"""
有一个整型数组 arr 和一个大小为 w 的窗口从数组的最左边滑到最右边,窗口每次向右边滑一个位置。 返回一个长度为n-w+1的数组res，res[i]表示每一种窗口状态下的最大值。 以数组为[4,3,5,4,3,3,6,7]，w=3为例。因为第一个窗口[4,3,5]的最大值为5，第二个窗口[3,5,4]的最大值为5，第三个窗口[5,4,3]的最大值为5。第四个窗口[4,3,3]的最大值为4。第五个窗口[3,3,6]的最大值为6。第六个窗口[3,6,7]的最大值为7。所以最终返回[5,5,5,4,6,7]。

给定整形数组arr及它的大小n，同时给定w，请返回res数组。保证w小于等于n，同时保证数组大小小于等于500。

测试样例：
[4,3,5,4,3,3,6,7],8,3
返回：[5,5,5,4,6,7]

"""


class SlideWindow:
    # 传统时间复杂度为O(n*w)
    def slide(self, arr, n, w):
        if not arr or w <= 0:
            return []

        length = n - w + 1
        res = []
        for i in range(length):
            temp_val = arr[i]

            for j in range(1, w):
                if temp_val < arr[i + j]:
                    temp_val = arr[i + j]

            res.append(temp_val)
        return res

    # 时间复杂度为O(n)：整个过程arr每个下标最多进双端队列一次，出双端队列一次
    def slide2(self, arr, n, w):

        from exceptions import ValueError

        class UnderFlow(ValueError):
            pass

        class LNode(object):

            def __init__(self, elem, prev=None, _next=None):
                self.elem = elem
                self.prev = prev
                self._next = _next

        class DoubleLList(object):

            def __init__(self):
                self.head = None
                self.rear = None

            def is_empty(self):
                return self.head == None

            def first(self):
                if self.is_empty():
                    raise UnderFlow('LList is empty')
                return self.head.elem

            def last(self):
                if self.is_empty():
                    raise UnderFlow('LList is empty')
                return self.rear.elem

            def prepend(self, elem):
                n = LNode(elem)
                if self.is_empty():
                    self.rear = n
                else:
                    n._next = self.head
                    self.head.prev = n
                self.head = n

            def append(self, elem):
                n = LNode(elem)
                if self.is_empty():
                    self.head = n
                else:
                    self.rear._next = n
                    n.prev = self.rear
                self.rear = n

            def prepop(self):
                if self.is_empty():
                    raise UnderFlow('LList is empty')

                elem = self.head.elem
                if self.head._next == None:
                    self.head = None
                    self.rear = None
                    return elem
                else:
                    self.head = self.head._next
                    self.head.prev = None
                    return elem

            def pop(self):
                if self.is_empty():
                    raise UnderFlow('LList is empty')

                elem = self.head.elem
                if self.head._next == None:
                    self.head = None
                    self.rear = None
                    return elem
                else:
                    self.rear = self.rear.prev
                    self.rear._next.prev = None
                    self.rear._next = None
                    return elem

            def traverse(self):
                current = self.head
                while current != None:
                    print current.elem
                    current = current._next

        res = []
        d = DoubleLList()
        for i in range(0, n):
            # 比较当前元素与双端队列（此处为双链表，方便起见）最后一个元素的大小：小的话直接追加，大的话先弹出所有较小元素再追加
            while not d.is_empty() and arr[i] >= arr[d.last()]:
                d.pop()

            d.append(i)

            # 弹出过期元素
            if i - d.first() >= w:
                d.prepop()

            # 追加窗口最大值
            if i >= w - 1:
                res.append(arr[d.first()])
        return res


s = SlideWindow()
# print s.slide2([36, 445, 234], 3, 1)
print s.slide2([4, 3, 5, 4, 3, 3, 6, 7], 8, 3)

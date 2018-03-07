#coding: utf-8

class LNode(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self._next = None


class SingleLinkList(object):
    def __init__(self):
        self.head = None

    @property
    def is_empty(self):
        return self.head == None

    def add(self, key, val):
        node = LNode(key, val)
        if self.is_empty:
            self.head = node
        else:
            current = unchange = self.head
            while current:
                if current.key == key:
                    current.val = val
                    return
                current = current._next
            self.head = node
            node._next = unchange

    def search(self, key):
        if self.is_empty:
            raise ValueError('LinkList is empty!')
        current = self.head
        while current:
            if current.key == key:
                return current.val
            current = current._next
        raise KeyError(key)

    def remove(self, key):
        # 单链表无节点，抛出异常
        if self.is_empty:
            raise KeyError(key)
        # 头节点即为要删除的节点
        if self.head.key == key:
            self.head = self.head._next
        # 向后查找要删除的节点
        else:
            prev = self.head
            current = self.head._next
            while current:
                if current.key == key:
                    prev._next = current._next
                    return
                prev = current
                current = current._next
            # 没有找到要删除的节点，抛出异常
            raise KeyError(key)



class dict(object):

    def __init__(self):
        self.n = 33
        self._list = []
        self.initialize()

    def initialize(self):
        for _ in range(self.n):
            self._list.append(SingleLinkList())

    def __hash(self, key):
        return hash(key) % self.n

    def put(self, key, val):
        m = self.__hash(key)
        self._list[m].add(key, val)

    def get(self, key):
        m = self.__hash(key)
        return self._list[m].search(key)

    def _delete(self, key):
        m = self.__hash(key)
        self._list[m].remove(key)


d = dict()
d.put('a', 1)
d.put('b', 2)
d.put('c', 3)
d.put('d', 4)
d.put('e', 5)
d.put('aseqqyw', 66)
d.put('aseqqywdfdsgjsedsfdssfer', 45)
d.put('e', 88)
d.put('esaer', 34)
d._delete('aseqqyw')
# d._delete('b')
# d._delete('aseqqywdfdsgjsedsfdssfer')
d._delete('e')
print d.get('c')



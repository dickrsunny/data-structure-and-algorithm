# coding: utf-8

class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val


class Dict(object):
    def __init__(self):
        self._list = [None] * 4
        # 字典中节点个数
        self.count = 0

    @property
    def length(self):
        return len(self._list)

    def __hash(self, key):
        return hash(key) % self.length

    def resize(self, length):
        new_list = [None] * length
        for i in xrange(self.length):
            if isinstance(self._list[i], Node):
                key, val = self._list[i].key, self._list[i].val
                m = hash(key) % length
                while True:
                    # 数组当前位置无节点或节点key为None
                    if not new_list[m]:
                        new_list[m] = self._list[i]
                        break
                    # 数组当前位置有节点且键等于key
                    elif new_list[m].key == key:
                        new_list[m].val = val
                        break
                    # 数组当前位置有节点且键不等于key
                    else:
                        m += 1
                        m = m % length
        self._list = new_list

    def put(self, key, val):
        if self.count >= self.length // 2:
            self.resize(self.length * 2)
        node = Node(key, val)
        m = self.__hash(key)
        while True:
            # 数组当前位置无节点或节点key为None
            if not self._list[m] or self._list[m] == -1:
                self._list[m] = node
                break
            # 数组当前位置有节点且键等于key
            elif self._list[m].key == key:
                self._list[m].val = val
                break
            # 数组当前位置有节点且键不等于key
            else:
                m += 1
                m = m % self.length
        self.count += 1

    def get(self, key):
        m = self.__hash(key)
        while self._list[m]:
            if isinstance(self._list[m], Node):
                if self._list[m].key == key:
                    return self._list[m].val
            m += 1
            m = m % self.length
        raise KeyError(key)

    def _delete(self, key):
        m = self.__hash(key)
        while self._list[m]:
            if isinstance(self._list[m], Node):
                if self._list[m].key == key:
                    self._list[m] = -1
                    self.count -= 1
                    if self.count > 0 and self.count == self.length // 8:
                        self.resize(self.length // 2)
                    return
            m += 1
            m = m % self.length
        raise KeyError(key)


d = Dict()
d.put(4, 0)
d.put(2, 0)
d.put(3, 0)
d.put(1, 0)
d.put(33, 0)
d.put(34, 0)
d.put(35, 1)
d.put(36, 0)
d._delete(33)
d._delete(1)
d._delete(2)
d._delete(3)
d._delete(4)
d._delete(34)
# d._delete(35)
d.put(49, 0)
# print d.get(35)

print ''

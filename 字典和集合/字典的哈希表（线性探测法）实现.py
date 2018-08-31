# coding: utf-8


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val


class Dict:
    def __init__(self):
        self._list = [None] * 4
        # 字典中节点个数
        self.count = 0

    def __len__(self):
        return len(self._list)

    def __getitem__(self, key):
        return self._get(key)

    def __setitem__(self, key, val):
        self._put(key, val)

    def _hash(self, key):
        return hash(key) % len(self)

    def _resize(self, length):
        new_list = [None] * length
        for i in range(len(self)):
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

    def _put(self, key, val):
        if self.count >= len(self) // 2:
            self._resize(len(self) * 2)

        node = Node(key, val)
        m = self._hash(key)

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
                m = m % len(self)
        self.count += 1

    def _get(self, key):
        m = self._hash(key)
        while self._list[m]:
            if isinstance(self._list[m], Node):
                if self._list[m].key == key:
                    return self._list[m].val
            m += 1
            m = m % len(self)
        raise KeyError(key)

    def pop(self, key, default=None):
        m = self._hash(key)
        while self._list[m]:
            if isinstance(self._list[m], Node):
                if self._list[m].key == key:
                    self._list[m] = -1
                    self.count -= 1
                    if self.count > 0 and self.count == len(self) // 8:
                        self._resize(len(self) // 2)
                    return
            m += 1
            m = m % len(self)

        if not default:
            raise KeyError(key)
        else:
            return default


d = Dict()
d[4] = 0
d[2] = 0
d[3] = 0
d[1] = 0

d[33] = 0
d[34] = 0
d[35] = 1
d[36] = 0

d.pop(33)
d.pop(1)
d.pop(2)
d.pop(3)
d.pop(4)
d.pop(34)
d.pop('rr', None)

print(d[35])

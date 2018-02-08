#coding: utf-8


class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val

    def __lt__(self, other):
        return self.key < other.key

    def __gt__(self, other):
        return self.key > other.key

    def __eq__(self, other):
        return self.key == other.key


class DictList(object):
    def __init__(self):
        self.elems = []

    @property
    def is_empty(self):
        return self.elems == []

    def binary_search_insert(self, node):
        low, high = 0, len(self.elems) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if node > self.elems[mid]:
                low = mid + 1
            elif node < self.elems[mid]:
                high = mid - 1
            else:
                return mid

        return low

    def insert(self, key, val):
        node = Node(key, val)
        if self.is_empty:
            self.elems.append(node)
        else:
            site = self.binary_search_insert(node)
            self.elems.insert(site, node)

    def binary_search_delete(self, key):
        low, high = 0, len(self.elems) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if key > self.elems[mid].key:
                low = mid + 1
            elif key < self.elems[mid].key:
                high = mid - 1
            else:
                return mid

    def delete(self, key):
        if not self.is_empty:
            site = self.binary_search_delete(key)
            if site:
                self.elems.pop(site)
            else:
                raise KeyError(key)
        else:
            raise KeyError(key)



d = DictList()
d.insert(1, 'q')
d.insert(3, 'q')
d.insert(5, 'q')
d.insert(7, 'q')
d.insert(2, 'q')
d.delete(99)


for i in d.elems:
    print i.key, i.val



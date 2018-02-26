#coding: utf-8

class Node(object):
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class Dict(object):
    def __init__(self):
        self.root = None

    @property
    def is_empty(self):
        return self.root == None

    def get(self, key):
        if self.is_empty:
            raise ValueError('dict is empty')

        return self.__get(key, self.root)

    def __get(self, key, root):
        if not root:
            return

        if key > root.key:
            return self.__get(key, root.right)
        elif key < root.key:
            return self.__get(key, root.left)
        else:
            return root.value

    def put(self, key, value):
        res = self.__put(key, value, self.root)
        if self.is_empty:
            self.root = res

    def __put(self, key, value, root):
        if not root:
            return Node(key, value)

        if key > root.key:
            root.right = self.__put(key, value, root.right)
        elif key < root.key:
            root.left = self.__put(key, value, root.left)
        else:
            root.value = value

        return root

    def delete_min(self):
        self.__delete_min(self.root)

    def __delete_min(self, root):
        if not root.left:
            return

        root.left = self.__delete_min(root.left)
        return root

    def delete(self, key):
        self.__delete(key, self.root)

    def __delete(self, key, root):
        if not root:
            return

        if key > root.key:
            root.right = self.__delete(key, root.right)
        elif key < root.key:
            root.left = self.__delete(key, root.left)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            new_root = self.delete_then_return_min(root.right)
            new_root.left = root.left
            if new_root != root.right:
                new_root.right = root.right
            return new_root
        return root

    def delete_then_return_min(self, root):
        prev = root
        while root.left:
            prev = root
            root = root.left

        prev.left = None
        return root

    def traverse(self):
        self.__traverse(self.root)

    def __traverse(self, root):
        if not root:
            return

        self.__traverse(root.left)
        print root.key, root.value
        self.__traverse(root.right)


d = Dict()
d.put(5, 'a')
d.put(3, 'a')
d.put(2, 'a')
d.put(1, 'a')
d.put(2.5, 'a')
d.put(4, 'a')
d.put(3.5, 'a')
d.put(4.5, 'a')
d.put(7, 'a')
d.put(6, 'a')
d.put(8, 'a')
d.put(7.5, 'a')
print d.get(8)
print ''
d.traverse()
d.delete_min()
d.delete(3)
print ''
d.traverse()





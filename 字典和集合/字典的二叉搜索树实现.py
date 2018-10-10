#coding: utf-8


'''
详情参考：https://github.com/julycoding/The-Art-Of-Programming-By-July/blob/master/ebook/zh/03.01.md
二叉查找树的删除
继续讲解之前，补充说明下二叉树结点删除的几种情况，待删除的结点按照儿子的个数可以分为三种：

1.没有儿子，即为叶结点。直接把父结点的对应儿子指针设为NULL，删除儿子结点就OK了。
2.只有一个儿子。那么把父结点的相应儿子指针指向儿子的独生子，删除儿子结点也OK了。
3.有两个儿子。这是最麻烦的情况，因为你删除结点之后，还要保证满足搜索二叉树的结构。
其实也比较容易，我们可以选择左儿子中的最大元素或者右儿子中的最小元素放到待删除结点的位置，
就可以保证结构的不变。当然，你要记得调整子树，毕竟又出现了结点删除。
习惯上大家选择左儿子中的最大元素，其实选择右儿子的最小元素也一样，没有任何差别，
只是人们习惯从左向右。这里咱们也选择左儿子的最大元素，将它放到待删结点的位置。
左儿子的最大元素其实很好找，只要顺着左儿子不断的去搜索右子树就可以了，
直到找到一个没有右子树的结点。那就是最大的了
'''


class Node:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

    def __gt__(self, other):
        return self.key > other.key

    def __lt__(self, other):
        return self.key < other.key


class Dict:
    def __init__(self):
        self.root = None

    @property
    def is_empty(self):
        return self.root is None

    def __getitem__(self, key):
        if self.is_empty:
            raise KeyError(key)

        node = Node(key, key)
        return self._get(node, self.root)

    def _get(self, node, root):
        if not root:
            raise KeyError(node.key)

        if node > root:
            return self._get(node, root.right)
        elif node < root:
            return self._get(node, root.left)
        else:
            return root.value

    def __setitem__(self, key, value):
        node = Node(key, value)
        if self.is_empty:
            self.root = node
        else:
            self._put(node, self.root)

    def _put(self, node, root):
        if not root:
            return node

        if node > root:
            root.right = self._put(node, root.right)
        elif node < root:
            root.left = self._put(node, root.left)
        else:
            root.value = node.value

        return root

    def pop_min(self):
        self._delete_min(self.root)

    def _delete_min(self, root):
        if not root.left:
            return

        root.left = self._delete_min(root.left)
        return root

    def pop(self, key, default=None):
        if self.is_empty:
            if not default:
                raise KeyError(key)
            else:
                return default

        node = Node(key, key)
        new_root = self._delete(node, self.root)

        # 删除根节点时替换根结点
        if key == self.root.key:
            self.root = new_root

    def _delete(self, node, root):
        if not root:
            raise KeyError(node.key)

        if node > root:
            root.right = self._delete(node, root.right)
        elif node < root:
            root.left = self._delete(node, root.left)
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

        prev.left = root.right
        return root

    def traverse(self):
        self._traverse(self.root)

    def _traverse(self, root):
        if not root:
            return

        self._traverse(root.left)
        print(root.key, root.value)
        self._traverse(root.right)


d = Dict()
d[5] = 'a'
d[3] = 'a'
d[2] = 'a'
d[1] = 'a'

d[2.5] = 'a'
d[4] = 'a'
d[3.5] = 'a'
d[4.5] = 'a'

d[7] = 'a'
d[6] = 'a'
d[8] = 'a'
d[7.5] = 'a'
d[8] = 'd'

print(d[8])
print('')
d.traverse()
d.pop_min()
d.pop(3)
print('')
d.traverse()

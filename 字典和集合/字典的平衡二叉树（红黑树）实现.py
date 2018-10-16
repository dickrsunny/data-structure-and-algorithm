# coding: utf-8

from collections import deque


class Node:
    def __init__(self, key, value=None, left=None, right=None, parent=None, color='red'):  # noqa
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.color = color
        self.parent = parent

    @property
    def is_red(self):
        return self.color == 'red'

    def set_color(self, color):
        if color not in ('red', 'black'):
            raise ValueError('{} is not valid color'.format(color))
        self.color = color

    def __lt__(self, other):
        return self.key < other.key

    def __gt__(self, other):
        return self.key > other.key

    def __eq__(self, other):
        return self.key == other.key


class Dict:
    def __init__(self):
        self.root = None

    @property
    def is_empty(self):
        return self.root is None

    def _get(self, node, root):
        if not root:
            raise KeyError(node.key)

        if node == root:
            return root.value
        elif node < root:
            return self._get(node, root.left)
        else:
            return self._get(node, root.right)

    def __getitem__(self, key):
        node = Node(key)
        return self._get(node, self.root)

    def left_rotate(self, node):
        """左旋"""
        child = node.right
        node.right = child.left
        if child.left:
            child.left.parent = node

        child.parent = node.parent
        if node.parent:
            if node == node.parent.left:
                node.parent.left = child
            else:
                node.parent.right = child
        else:
            self.root = child

        child.left = node
        node.parent = child

    def right_rotate(self, node):
        """右旋"""
        child = node.left
        node.left = child.right
        if child.right:
            child.right.parent = node

        child.parent = node.parent
        if node.parent:
            if node == node.parent.right:
                node.parent.right = child
            else:
                node.parent.left = child
        else:
            self.root = child

        child.right = node
        node.parent = child

    """插入实现"""
    def _insert_fix_up(self, node):
        """插入修正函数"""
        while node.parent and node.parent.parent and node.parent.is_red:
            parent = node.parent
            grand = parent.parent
            if parent == grand.left:
                uncle = grand.right
                # (1) 叔节点是红色
                if uncle.is_red:
                    # 父节点.和叔节点变黑，爷爷节点变红，不做旋转
                    parent.set_color('black')
                    uncle.set_color('black')
                    grand.set_color('red')
                    node = grand
                else:
                    # (2) 当前节点是父节点的右孩子
                    if node == parent.right:
                        # 以父节点左旋
                        self.left_rotate(parent)
                        node, parent = parent, node

                    # (3) 当前节点是父节点的左孩子
                    # 父节点变黑，爷爷节点变红，以爷爷节点右旋
                    parent.set_color('black')
                    grand.set_color('red')
                    self.right_rotate(grand)
            else:
                uncle = grand.left
                # (1) 叔节点是红色
                if uncle.is_red:
                    # 父节点和叔节点变黑，爷爷节点变红，不做旋转
                    parent.set_color("black")
                    uncle.set_color("black")
                    grand.set_color("red")
                    node = grand
                else:
                    # (2) 当前节点是父节点的左孩子
                    if node == parent.left:
                        # 以父节点右旋
                        self.right_rotate(parent)
                        node, parent = parent, node

                    # (3) 当前节点是父节点的右孩子
                    # 父节点变黑，爷爷节点变红，以爷爷节点左旋
                    parent.set_color("black")
                    grand.set_color("red")
                    self.left_rotate(grand)

    def _insert(self, node, root):
        """插入"""
        while root and node != root:
            parent = root

            if node < root:
                root = root.left
            else:
                root = root.right

        if not root:
            if node < parent:
                parent.left = node
            else:
                parent.right = node
            node.parent = parent

            # 父节点颜色为红色才需调整
            if parent.is_red:
                self._insert_fix_up(node)
                self.root.set_color('black')
        else:
            root.value = node.value

    def __setitem__(self, key, value):
        node = Node(key, value, color='red')
        if self.is_empty:
            node.set_color('black')
            self.root = node
        else:
            self._insert(node, self.root)

    """删除实现"""
    def find_min(self, root):
        """返回后继节点"""
        while root.left:
            root = root.left

        return root

    def _delete_fix_up(self):
        """删除修正函数"""
        node = self.child
        parent = self.parent

        while node and not node.is_red and (node != self.root):
            if parent.left == node:
                brother = parent.right
                # (1) 兄弟节点是红色
                if brother.is_red:
                    brother.set_color("black")
                    parent.set_color("red")
                    self.left_rotate(parent)
                    brother = parent.right
                # (2) 兄弟节点是黑色，且它的孩子都是黑色的
                if brother.left and not brother.left.is_red and brother.right and not brother.right.is_red:  # noqa
                    brother.set_color("red")
                    node = parent
                    parent = node.parent
                else:
                    # (3) 兄弟节点是黑色，且它的左孩子是红色，右孩子是黑色
                    if brother.left and brother.left.is_red and brother.right and not brother.right.is_red:  # noqa
                        brother.left.set_color("black")
                        brother.set_color("red")
                        self.right_rotate(brother)
                        brother = parent.right
                    # (4) 兄弟节点是黑色的，并且右孩子是红色的，左孩子颜色任意
                    brother.set_color(parent.color)
                    parent.set_color("black")
                    brother.right.set_color("black")
                    self.left_rotate(parent)
                    node = self.root
            else:
                brother = parent.left
                # (1) 兄弟节点是红色
                if brother.is_red:
                    brother.set_color("black")
                    parent.set_color("red")
                    self.right_rotate(parent)
                    brother = parent.left
                # (2) 兄弟节点是黑色，且它的孩子都是黑色的
                if brother.left and not brother.left.is_red and brother.right and not brother.right.is_red:  # noqa
                    brother.set_color("red")
                    node = parent
                    parent = node.parent
                else:
                    # (3) 兄弟节点是黑色，且它的左孩子是红色，右孩子是黑色
                    if brother.left and brother.left.is_red and brother.right and not brother.right.is_red:  # noqa
                        brother.right.set_color("black")
                        brother.set_color("red")
                        self.left_rotate(brother)
                        brother = parent.left
                    # (4) 兄弟节点是给色的，并且右孩子是红色的，左孩子颜色任意
                    brother.set_color(parent.color)
                    parent.set_color("black")
                    brother.left.set_color("black")
                    self.right_rotate(parent)
                    node = self.root

        if node:
            node.set_color("black")

    def _delete(self, node, root):
        if not root:
            raise KeyError(node.key)

        if node > root:
            root.right = self._delete(node, root.right)
        elif node < root:
            root.left = self._delete(node, root.left)
        else:
            self.parent = root.parent
            self.parent_color = root.color

            # 只有一个孩子，则返回孩子节点
            if not root.left or not root.right:
                self.child = root.right or root.left
                if self.child:
                    self.child.parent = self.parent

                return self.child

            # 当前root的后继节点
            new_root = self.find_min(root.right)
            self.parent = new_root.parent
            # 保存后继节点颜色
            self.parent_color = new_root.color
            self.child = new_root.right

            # 后继节点取代当前root并返回后继节点
            # 更新左子树
            new_root.left = root.left
            root.left.parent = new_root

            # 如果后继节点不是当前节点的右孩子
            if new_root != root.right:
                # 在右子树中删除后继节点
                if self.child:
                    self.child.parent = self.parent
                self.parent.left = self.child

                # 更新右子树
                new_root.right = root.right
                root.right.parent = new_root
            else:
                # 更新父节点为后继节点
                self.parent = new_root

            # 继承当前节点的颜色和父节点
            new_root.color = root.color
            new_root.parent = root.parent

            return new_root
        return root

    def pop(self, key, default=None):
        if self.is_empty:
            if not default:
                raise KeyError(key)
            else:
                return default

        node = Node(key, key)
        root = self._delete(node, self.root)

        # 删除根节点时替换根结点
        if node == self.root:
            self.root = root

        if self.parent_color == 'black':
            self._delete_fix_up()

    def traverse(self):
        if self.is_empty:
            return

        q = deque([self.root])
        last = self.root
        res, tmp = [], []
        while q:
            root = q.popleft()
            tmp.append('(key={}, color={}, parent={})'.format(
                    root.key, root.color, getattr(root.parent, 'key', None)
                )
            )

            if root.left:
                q.append(root.left)
            if root.right:
                q.append(root.right)

            if root == last:
                res.append(' '.join(tmp))
                tmp = []
                if q:
                    last = q[-1]

        for node in res:
            print(node)


d = Dict()
d[11] = 'val'
d[2] = 'val'
d[14] = 'val'
d[15] = 'val'
d[1] = 'val'
d[7] = 'val'
d[5] = 'val'
d[8] = 'val'
d[4] = 'val'
d.traverse()
d.pop(7)
print("\n")
d.traverse()
d.pop(8)
print("\n")
d.traverse()

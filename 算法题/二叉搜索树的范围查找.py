
class Node(object):
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.res = []

    def search_in_range(self, root, low, high):
        if not root:
            return

        if root.key > low:
            self.search_in_range(root.left, low, high)
        if low <= root.key <= high:
            self.res.append(root.key)
        if root.key < high:
            self.search_in_range(root.right, low, high)
        return self.res


tree = Node(3, 'a', Node(1, 'a', right=Node(2, 'a')), Node(5, 'a', Node(4, 'a'), Node(6, 'a')))
s = Solution()
print s.search_in_range(tree, 2, 5)
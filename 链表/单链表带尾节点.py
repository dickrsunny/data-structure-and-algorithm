from exceptions import ValueError

class OverFlow(ValueError):
    pass

class LNode(object):
    def __init__(self, elem, _next=None):
        self.elem = elem
        self._next = None


class LListWithTailNode(object):

    def __init__(self):
        self.head = None
        self.rear = None

    def is_empty(self):
        return self.head == None

    def prepend(self, elem):
        n = LNode(elem)
        if self.is_empty():
            self.head = n
            self.rear = n
        else:
            n._next = self.head
            self.head = n

    def append(self, elem):
        n = LNode(elem)
        if self.is_empty():
            self.head = n
            self.rear = n
        else:
            self.rear._next = n
            self.rear = n

    def prepop(self):
        if self.is_empty():
            raise OverFlow('LList is empty')
        current = self.head
        if current._next == None:
            elem = self.head.elem
            self.head = None
            self.rear = None
            return elem
        else:
            elem = self.head.elem
            self.head = self.head._next
            return elem

    def pop(self):
        if self.is_empty():
            raise OverFlow('LList is empty')
        current = self.head
        if current._next == None:
            elem = self.head.elem
            self.head = None
            self.rear = None
            return elem
        else:
            while current._next._next != None:
                current = current._next
            elem = current._next.elem
            current._next = None
            self.rear = current
            return elem

    def traverse(self):
        current = self.head
        while current != None:
            print current.elem
            current = current._next

    def reverse(self):
        prev = None
        current = self.head
        while current != None:
            next_node = current._next
            current._next = prev
            prev = current
            current = next_node
        self.head = prev

    def recursive_reverse(self, head=None):
        if head == None:
            return

        if head._next == None:
            return head

        new_head = self.recursive_reverse(head._next)
        head._next._next = head
        head._next = None
        self.head = new_head
        return new_head

    def sort(self):
        next_node = self.head._next
        while next_node != None:
            current = self.head
            while current != next_node:
                if next_node.elem < current.elem:
                    temp = next_node.elem
                    next_node.elem = current.elem
                    current.elem = temp
                current = current._next
            next_node = next_node._next


l = LListWithTailNode()
l.prepend(5)
l.prepend(2)
l.prepend(1)
l.prepend(3)
l.prepend(6)
l.prepend(7)
l.prepend(3)
l.traverse()
print ''
# l.recursive_reverse(l.head)
l.sort()
l.traverse()
# print l.rear.elem, '\n'
# l.append(5)
# l.append(6)
# l.traverse()
# print l.rear.elem





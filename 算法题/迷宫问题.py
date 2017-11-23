directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 1, 1],
    [1, 1, 0, 1, 0, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 1],
    [1, 1, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
]


def maze_with_recursive(list_, start, end):
    list_[start[0]][start[1]] = 2

    if start == end:
        print start
        return True

    for i in range(4):
        next_pos = (start[0] + directions[i][0], start[1] + directions[i][1])
        if list_[next_pos[0]][next_pos[1]] == 0:
            if maze_with_recursive(list_, next_pos, end):
                print start
                return True
    return False


from exceptions import ValueError

class UnderFlow(ValueError):
    pass

class Stack(object):

    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def push(self, elem):
        self.elems.append(elem)

    def pop(self):
        if self.is_empty():
            raise UnderFlow()
        elem = self.elems[-1]
        self.elems.pop()
        return elem


def maze_with_backtracking(list_, start, end):
    list_[start[0]][start[1]] = 2

    if start == end:
        print start
        return True

    s = Stack()
    s.push((start, 0))
    while not s.is_empty():
        elem, num = s.pop()
        for i in range(num, 4):
            next_step = (elem[0] + directions[i][0], elem[1] + directions[i][1])
            if list_[next_step[0]][next_step[1]] == 0:
                if next_step == end:
                    print next_step
                    return True
                print next_step
                s.push((elem, i + 1))
                s.push((next_step, 0))
                list_[next_step[0]][next_step[1]] = 2
                break
    return False


class Node(object):

    def __init__(self, elem):
        self.elem = elem
        self.next_ = None

class CircleSingleLList(object):

    def __init__(self):
        self.rear = None

    def is_empty(self):
        return self.rear == None

    def append(self, elem):
        node = Node(elem)
        if self.is_empty():
            node.next_ = node
            self.rear = node
        else:
            node.next_ = self.rear.next_
            self.rear.next_ = node
            self.rear = self.rear.next_

    def prepop(self):
        if self.is_empty():
            raise UnderFlow()

        if self.rear.next_ == self.rear:
            elem = self.rear.elem
            self.rear = None
            return elem
        else:
            elem = self.rear.next_.elem
            self.rear.next_ = self.rear.next_.next_
            return elem


class Queue(object):

    def __init__(self):
        self.c = CircleSingleLList()

    def is_empty(self):
        return self.c.is_empty()

    def enqueue(self, elem):
        self.c.append(elem)

    def dequeue(self):
        return self.c.prepop()


def maze_with_queue(list_, start, end):
    list_[start[0]][start[1]] = 2

    if start == end:
        print start
        return True

    q = Queue()
    q.enqueue(start)
    while not q.is_empty():
        elem = q.dequeue()
        for i in range(4):
            next_step = (elem[0] + directions[i][0], elem[1] + directions[i][1])
            if list_[next_step[0]][next_step[1]] == 0:
                if next_step == end:
                    print next_step
                    return True
                print next_step
                q.enqueue(next_step)
                list_[next_step[0]][next_step[1]] = 2
    return False


# maze_with_recursive(maze, (1, 1), (6, 6))
# maze_with_backtracking(maze, (1, 1), (6, 6))
maze_with_queue(maze, (1, 1), (6, 6))


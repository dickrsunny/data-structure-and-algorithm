
import heapq
from collections import deque


class Edge:
    def __init__(self, v1, v2, weight):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight


class Vertex:
    """ 记录每个顶点到起始点的距离 """
    def __init__(self, v, distance):
        self.v = v
        self.distance = distance

    def __lt__(self, other):
        return self.distance < other.distance


class PriorityQueue:
    """ 优先队列（小顶堆实现） """
    def __init__(self):
        self.array = []

    def enqueue(self, val):
        heapq.heappush(self.array, val)

    def dequeue(self):
        return heapq.heappop(self.array)

    def update(self):
        heapq.heapify(self.array)

    def is_empty(self):
        return self.array == []


class Graph:
    """ 采用邻接表的有向有权图 """

    def __init__(self, vertices):
        self.vertices = vertices
        self.adj = [deque() for i in range(vertices)]

    def add_edge(self, v1, v2, weight):
        """ 添加一条边 """
        self.adj[v1].append(Edge(v1, v2, weight))

    def _generate_path(self, v1, v2, prev, res):
            """ 生成路径 """
            if prev[v2] != -1 and v1 != v2:
                self._generate_path(v1, prev[v2], prev, res)

            res.append(str(v2))
            return res

    def dijkstra(self, v1, v2):
        """ 查找最短路径 """
        # 初始化各顶点到起始点的距离（默认为无穷大）
        vertexes = [Vertex(i, float("inf")) for i in range(self.vertices)]
        start = vertexes[v1]
        start.distance = 0

        # 使用优先队列（小顶堆）存储相邻顶点
        pq = PriorityQueue()
        pq.enqueue(start)

        # 标记顶点是否访问过
        visited = [False] * self.vertices
        visited[v1] = True

        # 记录当前顶点的前一个顶点
        prev = [-1] * self.vertices

        while not pq.is_empty():
            current_node = pq.dequeue()
            if current_node.v == v2:
                break

            for node in self.adj[current_node.v]:
                next_node = vertexes[node.v2]
                distance = current_node.distance + node.weight
                if distance < next_node.distance:
                    next_node.distance = distance
                    prev[node.v2] = current_node.v

                if visited[node.v2]:
                    pq.update()
                else:
                    pq.enqueue(next_node)
                    visited[node.v2] = True

        res = self._generate_path(v1, v2, prev, [])
        print("->".join(res))


g = Graph(6)
g.add_edge(0, 1, 10)
g.add_edge(0, 4, 15)
g.add_edge(1, 2, 15)
g.add_edge(1, 3, 2)
g.add_edge(2, 5, 5)
g.add_edge(3, 2, 1)
g.add_edge(3, 5, 12)
g.add_edge(4, 5, 10)
g.dijkstra(0, 5)

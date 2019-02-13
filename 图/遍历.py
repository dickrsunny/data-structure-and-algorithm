
from collections import deque
from queue import Queue


class Graph:
    """
        采用邻接表的无向图 
        采用deque（双链表）作为单链表存储相邻节点
    """
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj = [deque() for i in range(vertices)]

    def add_edge(self, v1, v2):
        """ 添加一条边 """
        self.adj[v1].append(v2)
        self.adj[v2].append(v1)

    def _generate_path(self, v1, v2, prev, res):
        """ 生成路径 """
        if prev[v2] != -1 and v1 != v2:
            self._generate_path(v1, prev[v2], prev, res)

        res.append(str(v2))
        return res

    def bfs(self, v1, v2):
        """ 广度优先遍历 """

        # 使用队列存储相邻顶点
        q = Queue()
        q.put(v1)

        # 标记顶点是否访问过
        visited = [False] * self.vertices
        visited[v1] = True

        # 记录当前顶点的前一个顶点
        prev = [-1] * self.vertices

        while not q.empty():
            current_v = q.get()
            # 遍历相邻顶点
            for v in self.adj[current_v]:
                if not visited[v]:
                    prev[v] = current_v
                    visited[v] = True
                    if v == v2:
                        res = self._generate_path(v1, v2, prev, [])
                        print("->".join(res))
                        return

                    q.put(v)

    def dfs(self, v1, v2):
        """ 深度优先遍历 """

        # 标记顶点是否访问过
        visited = [False] * self.vertices
        visited[v1] = True

        # 记录当前顶点的前一个顶点
        prev = [-1] * self.vertices

        self.found = False

        def recur_dfs(v1, v2):
            """ 递归查找 """
            if self.found:
                return

            visited[v1] = True

            if v1 == v2:
                self.found = True
                return

            for v in self.adj[v1]:
                if not visited[v]:
                    prev[v] = v1
                    recur_dfs(v, v2)

        recur_dfs(v1, v2)

        res = self._generate_path(v1, v2, prev, [])
        print("->".join(res))


g = Graph(8)

g.add_edge(0, 1)
g.add_edge(0, 3)
g.add_edge(1, 2)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(3, 4)
g.add_edge(4, 5)
g.add_edge(4, 6)
g.add_edge(5, 7)
g.add_edge(6, 7)

g.bfs(0, 7)
g.dfs(0, 7)

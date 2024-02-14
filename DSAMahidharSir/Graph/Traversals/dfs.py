class Graph:
    def __init__(self, vertices) -> None:
        self.vertices = vertices
        self.adj_list = {}

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = [v]
        else:
            self.adj_list[u].append(v)

        if v not in self.adj_list:
            self.adj_list[v] = [u]
        else:
            self.adj_list[v].append(u)

    def dfs(self,vis,node):
        self.vis = []
        if node not in vis:
            print(node)
            self.vis.append(node)
            for i in self.graph[node]:
                self.dfs(self.graph,vis,1)

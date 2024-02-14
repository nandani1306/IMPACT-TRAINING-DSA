class Graph:
    def __init__(self, vertices) -> None:
        self.vertices = vertices
        self.adj_list = {}

    def isVertex(self,vertex):
        return vertex < self.vertex and 0 <= vertex
    
    def add_edge(self, u, v):
        if not self.isVertex(u) or not self.isVertex(v):
            print("Source or Destination not available")
            return
        if u not in self.adj_list:
            self.adj_list[u] = [v]
        else:
            self.adj_list[u].append(v)

        if v not in self.adj_list:
            self.adj_list[v] = [u]
        else:
            self.adj_list[v].append(u)

    # def bfs(self, source):
    #     visited = []
    #     queue = [source]

    #     while queue:
    #         if queue[0] not in visited:
    #             visited.append(queue[0])
    #             print(queue[0], " ", end="")
            
    #         if queue[0] in self.adj_list:
    #             for node in self.adj_list[queue[0]]:
    #                 if node not in visited:
    #                     queue.append(node)
    #         queue.pop(0)
            
    def bfs(self,src):
        vis = []
        queue = [src]

        while queue:
            if queue[0] not in vis:
                vis.append(queue[0])
                print(queue[0], " ", end="")

            for node in self.adj_list[queue[0]]:
                if node not in vis:
                    queue.append(node)
            queue.pop(0)
    
    def print(self):
        for node in self.adj_list:
            print(node ,":", self.adj_list[node])

graph = Graph(6)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 5)
graph.add_edge(3, 4)
graph.add_edge(4, 2)


graph.bfs(0)
print()
graph.print()

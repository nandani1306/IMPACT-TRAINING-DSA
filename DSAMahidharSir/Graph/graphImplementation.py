# class Vertex:
#     def __init__(self,data) -> None:
#         self.data = data 
#         self.next = None

# BFS = LEVEL ORDER TRAVERSAL
        
class Graph:
    # def __init__(self,num) -> None:
    #     self.vertices = num
    #     self.graph = [None] * self.vertices

    # def addEdges(self, src, dest):
    #     ver = Vertex(dest)
    #     ver.next = self.graph[src]
    #     self.graph[src] = ver

    #     ver = Vertex(src)
    #     ver.next = self.graph[dest]
    #     self.graph[dest] = ver

    # def printGraph(self):


    def __init__(self,vertex) -> None:
        self.vertex = vertex
        # self.matrix = [[None for _ in range(vertex)] for _ in range(vertex)]
        self.matrix=[[0]*self.vertex for _ in range(self.vertex)]
        for i in range(vertex):
            for j in range(vertex):
                if i == j:
                    self.matrix[i][j] = 0

    def isVertex(self,vertex):
        return vertex < self.vertex and 0 <= vertex

    def addEdge(self,u,v):
        if not self.isVertex(u) or not self.isVertex(v):
            print("Source or Destination not available")
            return
        else:
            if self.matrix[u][v] == 0:
                self.matrix[u][v] = 1
                self.matrix[v][u] = 1 
            else:
                raise(ValueError)
            
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
            
    def removeEdge(self,u,v):
        if not self.isVertex(u) or not self.isVertex(v):
            print("Source or Destination not available")
            return
        else:
            if self.matrix[u][v] == 1:
                self.matrix[u][v] = 0
                self.matrix[v][u] = 0
            else:
                raise(ValueError)
            
    def printGraph(self):
        for vertex in self.matrix:
            print(*vertex)

    
            
gr = Graph(6)
gr.addEdge(0, 2)
gr.addEdge(2, 3)
gr.addEdge(3, 1)
gr.addEdge(4, 5)
gr.addEdge(3, 4)
gr.removeEdge(4, 5)
gr.bfs(0)
gr.printGraph()
    
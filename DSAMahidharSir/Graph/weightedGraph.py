class Graph:
    def __init__(self,vertex) -> None:
        self.vertex = vertex
        # self.matrix = [[None for _ in range(vertex)] for _ in range(vertex)]
        self.matrix=[[float('inf')]*self.vertex for _ in range(self.vertex)]
        for i in range(vertex):
            for j in range(vertex):
                if i == j:
                    self.matrix[i][j] = 0

    def isVertex(self,vertex):
        return vertex < self.vertex and 0 <= vertex

    def addEdge(self,u,v,wt=1):
        if not self.isVertex(u) or not self.isVertex(v):
            print("Source or Destination not available")
            return
        else:
            # if self.matrix[u][v] == 0:
            self.matrix[u][v] = wt
            self.matrix[v][u] = wt
        # else:
        #     raise(ValueError)
            
    def removeEdge(self,u,v):
        if not self.isVertex(u) or not self.isVertex(v):
            print("Source or Destination not available")
            return
        else:
            if self.matrix[u][v] is not float('inf'):
                self.matrix[u][v] = float('inf')
                self.matrix[v][u] = float('inf')
            else:
                raise(ValueError)
            
    def printGraph(self):
        for vertex in self.matrix:
            print(*vertex)

gr = Graph(6)
gr.addEdge(1, 2)
gr.addEdge(2, 3)
gr.addEdge(3, 1)
gr.addEdge(4, 5)

gr.printGraph()
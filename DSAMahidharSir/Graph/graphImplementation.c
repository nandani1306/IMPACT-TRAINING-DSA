#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

typedef struct graph{
    int totalVertices;
    int totalEdges;
    int** adjList;
} Graph;

Graph* getGraph(int totalVertices){
    Graph* graph = (Graph*)malloc(sizeof(Graph));
    graph->totalVertices = totalVertices;
    graph->totalEdges = 0;
    graph->adjList = (int**)malloc(sizeof(int*)*graph->totalEdges);
    // printf("Graph created");
    return graph;
}

bool isVertex(Graph* graph, int u){
    return graph->totalVertices > u;
}

void addEdge(Graph* graph, int u, int v){
    if(!isVertex(graph,u) || !isVertex(graph,v)){
        printf("ValueError : Vertex doesn't exists\n");
        return;
    }
    else{
        graph->adjList = realloc(graph->adjList, sizeof(int*)*(++graph->totalEdges));
        graph->adjList[graph->totalEdges-1] = (int*)malloc(sizeof(int)*2);
        graph->adjList[graph->totalEdges-1][0] = u;
        graph->adjList[graph->totalEdges-1][1] = v;
    }
}

void removeEdge(Graph* graph, int u, int v){
    if(!isVertex(graph,u) || !isVertex(graph,v)){
        printf("ValueError : Vertex doesn't exists\n");
        return;
    }
    else{
        for (int i = 0; i < graph->totalEdges; i++)
        {
            if(graph->adjList[i][0] == u && graph->adjList[i][1] == v){
                graph->adjList[i][0] = graph->adjList[graph->totalEdges-1][0];
                graph->adjList[i][1] = graph->adjList[graph->totalEdges-1][1];
                graph->adjList = realloc(graph->adjList, sizeof(int*)*(--graph->totalEdges));
            }
        }   
    }
}

void freeGraph(Graph* graph){
    for (int i = 0; i < graph->totalEdges; i++){
        free(graph->adjList[i]);
    }
    free(graph->adjList);
    free(graph);
}

void printGraph(Graph* graph){
    if(!graph){
        return;
    }
    else{
        for(int i = 0; i < graph->totalEdges; i++){
            printf("[%d, %d]\n",graph->adjList[i][0], graph->adjList[i][1]);
        }
        printf("\n");
    }
}

int main(){
    Graph* graph = getGraph(6);
    addEdge(graph, 1, 2);
    addEdge(graph, 2, 3);
    addEdge(graph, 3, 1);
    addEdge(graph, 4, 1);
    addEdge(graph, 5, 1);
    addEdge(graph, 3, 4);

    removeEdge(graph, 2, 3);
    printGraph(graph);
    return 0;
}

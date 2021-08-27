def graphZero(graph,n):
    for i in range(n):
        x=[]
        for j in range(n):
            x.append(0)
        graph.append(x)

def graphMatrix(graph, m):
    for i in range(m):
        p=int(input('\nWprowadz p: '))
        k=int(input('\nWprowadz k: '))
        graph[p][k]= 1
    return graph

def mn(A,B):
    n=len(A)
    x = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                x[i][j] = x[i][j] + A[i][k] * B[k][j]
    return (x)

def gr(k,graph):
    l=[]
    l.append(graph)
    if k==1:
        result=graph
    else:
        for i in range(k-1):
            result=mn(l[i],graph)
            l.append(result)
    return (result)

graph=[]
vertex=int(input('\nWprowadz wierzchołki: '))
edges=int(input('\nWprowadz krawędzie: '))
graphZero(graph, vertex)
graphMatrix(graph, edges)
n=len(graph)
k=int(input("\nWprowadz długości szukanych marszrut: "))
k_graf=gr(k,graf)
u=int(input("\nz wierzchołka "))
v=int(input("\ndo wierzchołka "))
print("\nwynosi ",k_graf[u][v])

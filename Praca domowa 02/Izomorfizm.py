def Isomorphic(g1,g2):
    for i in range(len(g1)):
        for j in range(len(g2)):
            if g1[i]==g2[j] and i!=j: #zamieniamy wiersze
                tmp=g2[i] 
                g2[i]=g2[j]
                g2[j]=tmp
                for k in range(len(g1)): #zamieniamy kolumny
                    if k!=i and k!=j:
                        t=g2[k][i]
                        g2[k][i]=g2[k][j]
                        g2[k][j]=t
    if g1==g2:
        print("Podane drzewa sa izomorficzne")
    else:
        print("Podane drzewa nie sa izomorficzne")

graph1 = [[0,1,0,0,0,0,0],[1,0,0,0,1,0,0],[0,0,0,1,1,0,0],[0,0,1,0,0,0,0],[0,1,1,0,0,1,0],[0,0,0,0,1,0,1],[0,0,0,0,0,1,0]]
graph2 = [[0,1,1,0,0,0,0],[1,0,0,0,0,1,0],[1,0,0,1,1,0,0],[0,0,1,0,0,0,0],[0,0,1,0,0,0,1],[0,1,0,0,0,0,0],[0,0,0,0,1,0,0]]
graph3 = [[0,1,1,0,0,1,0],[1,0,0,0,1,0,0],[1,0,0,1,0,0,0],[0,0,1,0,0,0,0],[0,1,0,0,0,0,0],[1,0,0,0,0,0,1],[0,0,0,0,0,1,0]]

Isomorphic(graph1, graph2)
Isomorphic(graph1, graph3)
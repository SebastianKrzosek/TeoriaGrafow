def cycle(Graph):
    colors = []
    for i in enumerate(Graph):
        colors.append("white")
    cycle = False
    for u in Graph:
        if colors[u] == "white":
            cycle = dfs(Graph, u, colors, cycle)
        if cycle:
            return cycle
    return cycle
 

def dfs(Graph, u, colors, cycle):
    if cycle:
        return cycle
    colors[u] = "gray" 
    for v in Graph[u]:
        if colors[v] == "gray":
            cycle = True
            return cycle
        if colors[v] == "white":
            cycle = dfs(Graph, v, colors, cycle)
    return cycle

if __name__ == "__main__":
    graph1= { 0 : [1, 2],
            1 : [3, 4],
            2 : [5],
            3 : [],
            4 : [6],
            5 : [7],
            6 : [],
            7 : []}

    graph2 = { 0 : [1, 2],
            1 : [3, 4],
            2 : [5],
            3 : [],
            4 : [5, 6],
            5 : [7],
            6 : [4],
            7 : [6]}

    if cycle(graph1):
        print("Pierwszy digraf jest cykliczny")
    else:
        print("Pierwszy digraf jest acykliczny")

    if cycle(graph2):
        print("Drugi digraf jest cykliczny")
    else:
        print("Drugi digraf jest acykliczny")
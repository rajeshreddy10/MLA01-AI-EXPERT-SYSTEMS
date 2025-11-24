def graph_coloring(graph, colors, node=0, solution=[]):
    if node == len(graph):
        print("Coloring:", solution)
        return True
    for color in colors:
        if all(color != solution[i] for i in graph[node] if i < len(solution)):
            if graph_coloring(graph, colors, node+1, solution + [color]):
                return True
    return False

graph = [[1,2], [0,2,3], [0,1,3], [1,2]]  # adjacency list
colors = [1,2,3]  # 3 colors
graph_coloring(graph, colors)

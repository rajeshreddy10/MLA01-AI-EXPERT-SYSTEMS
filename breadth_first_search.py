graph = {
 'A': ['B','C'],
 'B': ['D','E'],
 'C': ['F'],
 'D': [],
 'E': ['F'],
 'F': []
}

visited = []
queue = ['A']

while queue:
    node = queue[0]
    queue = queue[1:]
    if node not in visited:
        print(node, end=' ')
        visited += [node]
        queue += graph[node]

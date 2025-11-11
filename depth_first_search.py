graph = {
 'A': ['B','C'],
 'B': ['D','E'],
 'C': ['F'],
 'D': [],
 'E': ['F'],
 'F': []
}

visited = []

def dfs(node):
    if node not in visited:
        print(node, end=' ')
        visited.append(node)
        for n in graph[node]:
            dfs(n)

dfs('A')

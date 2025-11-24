import heapq

graph = {
    'A': {'B':1,'C':4},
    'B': {'D':3,'E':5},
    'C': {'F':2},
    'D': {'F':1,'E':1},
    'E': {'F':2},
    'F': {}
}

heuristic = {'A':5,'B':4,'C':2,'D':1,'E':1,'F':0}

def a_star(start, goal):
    open_set = [(0+heuristic[start], 0, start, [start])]
    while open_set:
        f, g, node, path = heapq.heappop(open_set)
        if node == goal:
            return path, g
        for neigh, cost in graph[node].items():
            heapq.heappush(open_set, (g+cost+heuristic[neigh], g+cost, neigh, path+[neigh]))
            
path, cost = a_star('A','F')
print("A* Path:", path, "Cost:", cost)

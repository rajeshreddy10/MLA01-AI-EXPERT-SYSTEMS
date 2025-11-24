import heapq

graph = {
    'A':{'B':1,'C':4},
    'B':{'D':3,'E':5},
    'C':{'F':2},
    'D':{'F':1,'E':1},
    'E':{'F':2},
    'F':{}
}

def ucs(start, goal):
    pq = [(0, start, [start])]
    visited = set()
    while pq:
        cost, node, path = heapq.heappop(pq)
        if node==goal: return path, cost
        if node in visited: continue
        visited.add(node)
        for neigh,w in graph[node].items():
            heapq.heappush(pq, (cost+w, neigh, path+[neigh]))
        
path, cost = ucs('A','F')
print("UCS Path:", path, "Cost:", cost)

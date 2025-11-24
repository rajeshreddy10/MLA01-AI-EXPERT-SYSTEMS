import numpy as np

dist = np.array([[0,2,2,5],[2,0,3,2],[2,3,0,3],[5,2,3,0]])
n=4; pheromone=np.ones((n,n)); alpha=1; beta=2; evaporation=0.5
best_path=[]; best_cost=float('inf')

for _ in range(50):
    paths=[]
    costs=[]
    for _ in range(10):
        path=[0]; visited={0}
        while len(path)<n:
            probs=[]
            last=path[-1]
            for j in range(n):
                if j not in visited:
                    probs.append((j,(pheromone[last,j]**alpha)*(1/dist[last,j])**beta))
            j=max(probs,key=lambda x:x[1])[0]
            path.append(j); visited.add(j)
        path.append(0)
        cost=sum(dist[path[i],path[i+1]] for i in range(n))
        paths.append(path); costs.append(cost)
    best_idx=np.argmin(costs)
    if costs[best_idx]<best_cost: best_cost=costs[best_idx]; best_path=paths[best_idx]
    pheromone*=1-evaporation
    for i in range(n): pheromone[best_path[i],best_path[i+1]]+=1/best_cost

print("Best ACO path:", best_path, "Cost:", best_cost)

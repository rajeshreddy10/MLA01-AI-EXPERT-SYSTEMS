import itertools

cities = ['A','B','C','D']
dist = {('A','B'):10,('A','C'):15,('A','D'):20,
        ('B','C'):35,('B','D'):25,
        ('C','D'):30}

def distance(path):
    return sum(dist.get((path[i],path[i+1]), dist.get((path[i+1],path[i]))) for i in range(len(path)-1)) + dist.get((path[-1],path[0]), dist.get((path[0],path[-1])))

best_path = min(itertools.permutations(cities), key=distance)
print("Best TSP path:", best_path, "Cost:", distance(best_path))

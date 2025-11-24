def beam_search(graph, start, goal, beam_width, heuristic):
    paths = [[start]]
    while paths:
        new_paths = []
        for path in paths:
            for n in graph[path[-1]]:
                if n not in path: new_paths.append(path+[n])
        paths = sorted(new_paths, key=lambda p: heuristic[p[-1]])[:beam_width]
        for path in paths:
            if path[-1]==goal: return path
    return None

graph = {'A':['B','C'],'B':['D','E'],'C':['F'],'D':['F','E'],'E':['F'],'F':[]}
heuristic = {'A':5,'B':4,'C':2,'D':1,'E':1,'F':0}
print("Beam search path:", beam_search(graph,'A','F',2,heuristic))

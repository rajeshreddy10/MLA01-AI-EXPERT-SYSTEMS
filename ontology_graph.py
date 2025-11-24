triples=[('Cat','Animal'),('Dog','Animal'),('Animal','LivingBeing')]
graph={}
for sub,sup in triples:
    graph.setdefault(sup,[]).append(sub)

def subclasses(cls):
    res=[]
    if cls in graph:
        for c in graph[cls]:
            res.append(c)
            res+=subclasses(c)
    return res

def is_subclass(sub,sup):
    return sub in subclasses(sup)

print("Subclasses of Animal:", subclasses('Animal'))
print("Is Cat subclass of LivingBeing?", is_subclass('Cat','LivingBeing'))

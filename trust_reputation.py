providers={'A':[],'B':[],'C':[]}
clients=[('A',1),('B',0),('C',1),('A',1),('B',1)]
for p,r in clients: providers[p].append(r)
reputation={p:sum(v)/len(v) for p,v in providers.items()}
best=max(reputation,key=reputation.get)
print("Reputation:", reputation, "Best provider:", best)

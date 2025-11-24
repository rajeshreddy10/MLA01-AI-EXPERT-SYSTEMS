def negotiate(rounds=10):
    offer = [50,50]; delta = [0.9,0.9]
    for r in range(rounds):
        if r%2==0: offer[0]+=1; offer[1]-=1  # Agent 1 proposes
        else: offer[1]+=1; offer[0]-=1       # Agent 2 proposes
        if offer[0]>=50 and offer[1]>=50: break
        offer = [x*delta[r%2] for x in offer]
    print("Final agreement:", offer)

negotiate()

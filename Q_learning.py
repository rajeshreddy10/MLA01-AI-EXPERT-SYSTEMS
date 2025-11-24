import numpy as np, random

grid=np.zeros((5,5))
start=(0,0); goal=(4,4); obstacles=[(1,1),(2,2)]
actions=[(0,1),(1,0),(0,-1),(-1,0)]
Q=np.zeros((5,5,4))
alpha=0.1; gamma=0.9; epsilon=0.2

for _ in range(1000):
    state=start
    while state!=goal:
        if random.random()<epsilon: a=random.randint(0,3)
        else: a=np.argmax(Q[state[0],state[1]])
        next_state=(state[0]+actions[a][0],state[1]+actions[a][1])
        if 0<=next_state[0]<5 and 0<=next_state[1]<5 and next_state not in obstacles:
            reward=1 if next_state==goal else -0.1
            Q[state[0],state[1],a]+=alpha*(reward+gamma*max(Q[next_state[0],next_state[1]])-Q[state[0],state[1],a])
            state=next_state
        else: reward=-0.1
print("Learned Q-table:\n", Q)

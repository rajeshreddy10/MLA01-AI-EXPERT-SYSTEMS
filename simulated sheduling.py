import random, math

tasks = [1,2,3,4,5,6]; slots = [0,1,2]
def cost(schedule):
    return sum(schedule.count(s)>2 for s in slots)  # penalty if slot exceeds capacity

schedule = [random.choice(slots) for _ in tasks]
T=10; alpha=0.95
best, best_cost = schedule[:], cost(schedule)
for _ in range(1000):
    i=random.randint(0,len(tasks)-1)
    new_schedule = schedule[:]; new_schedule[i] = random.choice(slots)
    delta = cost(new_schedule)-cost(schedule)
    if delta<0 or random.random()<math.exp(-delta/T):
        schedule = new_schedule
    T*=alpha
    if cost(schedule)<best_cost: best,best_cost=schedule[:],cost(schedule)
print("Best schedule:", best, "Cost:", best_cost)

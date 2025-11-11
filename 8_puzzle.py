puzzle = [[7, 2, 4],
          [5, 0, 6],
          [8, 3, 1]]
flat = [n for row in puzzle for n in row]
for i in range(len(flat)):
    for j in range(len(flat) - 1):
        if flat[j] == 0 or flat[j + 1] == 0:
            continue
        if flat[j] > flat[j + 1]:
            flat[j], flat[j + 1] = flat[j + 1], flat[j]
flat = sorted([n for n in flat if n != 0]) + [0]
puzzle = [flat[i:i + 3] for i in range(0, 9, 3)]
print("Sorted 8-Puzzle (Goal State):")
for row in puzzle:
    print(row)

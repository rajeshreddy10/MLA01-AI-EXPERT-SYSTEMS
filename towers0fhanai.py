def hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from {source} → {target}")
        return
    # Move n-1 disks from source to auxiliary
    hanoi(n-1, source, target, auxiliary)
    # Move the largest disk from source to target
    print(f"Move disk {n} from {source} → {target}")
    # Move the n-1 disks from auxiliary to target
    hanoi(n-1, auxiliary, source, target)

n = 3
print(f"Towers of Hanoi solution for {n} disks:\n")
hanoi(n, 'A', 'B', 'C')

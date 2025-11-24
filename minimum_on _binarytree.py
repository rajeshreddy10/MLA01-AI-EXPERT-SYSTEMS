def minimax(node, depth, maximizing, tree):
    if depth == len(tree[node]):
        return tree[node]
    if maximizing:
        return max(minimax(child, depth+1, False, tree) for child in tree[node])
    else:
        return min(minimax(child, depth+1, True, tree) for child in tree[node])

# Tree as adjacency with leaf values at depth 2
tree = {0:[1,2], 1:[3,4], 2:[5,6], 3: [3], 4: [5], 5: [2], 6: [9]}  # last numbers are leaf values
print("Best value for maximizing player:", minimax(0, 0, True, tree))

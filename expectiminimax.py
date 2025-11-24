def expectiminimax(node, tree_type, tree):
    if type(tree[node])==int: return tree[node]
    if tree_type[node]=='Max':
        return max(expectiminimax(c, tree_type, tree) for c in tree[node])
    if tree_type[node]=='Min':
        return min(expectiminimax(c, tree_type, tree) for c in tree[node])
    if tree_type[node]=='Chance':
        return sum(0.5*expectiminimax(c, tree_type, tree) for c in tree[node])  # equal prob

tree = {0:[1,2], 1:[3,4], 2:[5,6], 3:3,4:5,5:2,6:9}
tree_type = {0:'Max',1:'Min',2:'Min',3:'Leaf',4:'Leaf',5:'Leaf',6:'Leaf'}
print("Expectiminimax value:", expectiminimax(0, tree_type, tree))

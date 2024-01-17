import re

input = open('input2.txt').read().splitlines()

weights = {}
G = {}
G_Rev = {}
for line in input:
    weight = int(re.findall(r'\d+', line)[0])
    name = line.split(' ')[0]
    weights[name] = weight
    if name not in G:
        G[name] = []
        G_Rev[name] = []

    if '->' not in line:
        continue

    children = line.split(' -> ')[1].split(', ')
    for child in children:
        if child not in G:
            G[child] = []
            G_Rev[child] = []
        G_Rev[child].append(name)
        G[name].append(child)

root = ''
for parent, children in G_Rev.items():
    if len(children) == 0:
        root = parent
        break

def get_balancing_value(G: dict, node: str, weights: dict) -> tuple:
    current_weight = weights[node]
    children_weights = {}
    for child in G[node]:
        child_weight, child_balancing_value = get_balancing_value(G, child, weights)
        if child_balancing_value != None:
            return (0, child_balancing_value)
        current_weight += child_weight
        if child_weight not in children_weights:
            children_weights[child_weight] = [0, child]
        children_weights[child_weight][0] += 1
    
    if len(children_weights.items()) == 2:
        not_balanced_value, (_, child) = [y for y in filter(lambda x: x[1][0] == 1, children_weights.items())][0]
        not_balanced_value -= weights[child]
        balanced_value, _ = [y for y in filter(lambda x: x[1][0] != 1, children_weights.items())][0]
        return (0, balanced_value - not_balanced_value)
        
    
    return (current_weight, None)

print(get_balancing_value(G, root, weights)[1])
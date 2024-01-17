import re

input = open('input2.txt').read().splitlines()

weights = {}
G = {}
for line in input:
    weight = int(re.findall(r'\d+', line)[0])
    name = line.split(' ')[0]
    weights[name] = weight
    if name not in G:
        G[name] = []

    if '->' not in line:
        continue

    children = line.split(' -> ')[1].split(', ')
    for child in children:
        if child not in G:
            G[child] = []
        G[child].append(name)

result = ''
for parent, children in G.items():
    if len(children) == 0:
        result = parent
        break

print(result)
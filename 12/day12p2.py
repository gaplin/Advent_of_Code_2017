import re

def mark_reachable_nodes(G: dict, u: int, visited: set) -> int:
    visited.add(u)
    for v in G[u]:
        if v not in visited:
            mark_reachable_nodes(G, v, visited)
    
    return result

input = open('input2.txt').read().splitlines()

G = {}
for line in input:
    nums = [int(x) for x in re.findall(r'\d+', line)]
    for num in nums:
        if num not in G:
            G[num] = []

    for num in nums[1:]:
        G[num].append(nums[0])
        G[nums[0]].append(num)

marked_nodes = set()
result = 0
for u in G.keys():
    if u not in marked_nodes:
        mark_reachable_nodes(G, u, marked_nodes)
        result += 1
        
print(result)
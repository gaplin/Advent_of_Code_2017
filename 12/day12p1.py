import re

def get_reachable_count(G: dict, u: int, visited: set) -> int:
    result = 1
    visited.add(u)
    for v in G[u]:
        if v not in visited:
            result += get_reachable_count(G, v, visited)
    
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

result = get_reachable_count(G, 0, set())
print(result)
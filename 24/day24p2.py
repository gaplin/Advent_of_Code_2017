def get_max(connectors: dict, visited: set, current: tuple) -> tuple:
    result = [0, 0]

    visited.add(current[2])
    for a, b, idx in connectors[current[1]]:
        if idx not in visited:
            length, strength = get_max(connectors, visited, (a, b, idx))
            strength += a + b
            if length + 1 > result[0] or (length + 1 == result[0] and strength > result[1]):
                result[0], result[1] = length + 1, strength

    visited.remove(current[2])
    return tuple(result)


input = open('input2.txt').read().splitlines()
n = len(input)
connectors = {}
for i, line in enumerate(input):
    nums = [int(x) for x in line.split('/')]
    for a, b in [(nums[0], nums[1]), (nums[1], nums[0])]:
        if a not in connectors:
            connectors[a] = []
        connectors[a].append((a, b, i))

print(get_max(connectors, set(), (0, 0, -1))[1])

input = open('input2.txt').read().splitlines()
n = len(input)

infected = set()
for i in range(n):
    for ii in range(n):
        if input[i][ii] == '#':
            infected.add((i, ii))

left_turn = lambda x, y: (-y, x)
right_turn = lambda x, y: (y, -x)

position = (n // 2, n // 2)
direction = (-1, 0)

iterations = 10000
result = 0
for i in range(iterations):
    if position in infected:
        direction = right_turn(*direction)
        infected.remove(position)
    else:
        direction = left_turn(*direction)
        infected.add(position)
        result += 1
    position = (position[0] + direction[0], position[1] + direction[1])

print(result)
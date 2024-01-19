input = open('input2.txt').read().splitlines()
n = len(input)

infected = set()
weakened = set()
flagged = set()
for i in range(n):
    for ii in range(n):
        if input[i][ii] == '#':
            infected.add((i, ii))

left_turn = lambda x, y: (-y, x)
right_turn = lambda x, y: (y, -x)
reverse_turn = lambda x, y: (-x, -y)

position = (n // 2, n // 2)
direction = (-1, 0)

iterations = 10000000
result = 0
for i in range(iterations):
    if position in infected:
        direction = right_turn(*direction)
        infected.remove(position)
        flagged.add(position)
    elif position in flagged:
        direction = reverse_turn(*direction)
        flagged.remove(position)
    elif position in weakened:
        weakened.remove(position)
        infected.add(position)
        result += 1
    else:
        direction = left_turn(*direction)
        weakened.add(position)
    position = (position[0] + direction[0], position[1] + direction[1])

print(result)
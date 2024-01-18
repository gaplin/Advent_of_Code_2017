from queue import Queue

directions = {
    'n': (0, 2),
    's': (0, -2),
    'nw': (-1, 1),
    'ne': (1, 1),
    'sw': (-1, -1),
    'se': (1, -1)
}

moves = open('input2.txt').read().strip().split(',')

position = [0, 0]

for move in moves:
    dx, dy = directions[move]
    position[0] += dx
    position[1] += dy

print((abs(position[0]) + abs(position[1])) // 2)
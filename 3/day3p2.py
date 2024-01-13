from math import ceil, sqrt

num = int(open('input2.txt').read().strip())

n = ceil(sqrt(num))
n += (1 - n % 2)
grid = [[0 for _ in range(n)] for _ in range(n)]

def fill_value(grid: list, n: int, i: int, ii: int, directions: list) -> int:
    value = 0
    for di, dii in directions:
        new_i, new_ii = i + di, ii + dii
        if new_i < 0 or new_i >= n or new_ii < 0 or new_ii >= n:
            continue
        value += grid[new_i][new_ii]
    grid[i][ii] = value
    return value

current_position = [n // 2, n // 2]
grid[n // 2][n // 2] = 1
directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
for k in range(3, n + 1, 2):
    current_position[1] += 1
    for i in range(k - 1):
        value = fill_value(grid, n, *current_position, directions)
        if value > num:
            print(value)
            exit()
        current_position[0] -= 1
    else:
        current_position[0] += 1
        current_position[1] -= 1
    for i in range(k - 1):
        value = fill_value(grid, n, *current_position, directions)
        if value > num:
            print(value)
            exit()
        current_position[1] -= 1
    else:
        current_position[1] += 1
        current_position[0] += 1
    for i in range(k - 1):
        value = fill_value(grid, n, *current_position, directions)
        if value > num:
            print(value)
            exit()
        current_position[0] += 1
    else:
        current_position[0] -= 1
        current_position[1] += 1
    for i in range(k - 1):
        value = fill_value(grid, n, *current_position, directions)
        if value > num:
            print(value)
            exit()
        current_position[1] += 1
    else:
        current_position[1] -= 1
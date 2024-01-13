from math import ceil, sqrt

num = int(open('input2.txt').read().strip())

n = ceil(sqrt(num))
n += (1 - n % 2)
grid = [[0 for _ in range(n)] for _ in range(n)]

current_position = [n // 2, n // 2 - 1]
current_num = 1
for k in range(1, n + 1, 2):
    current_position[1] += 1
    if k == 1:
        grid[current_position[0]][current_position[1]] = current_num
        current_num += 1
        continue
    for i in range(k - 1):
        grid[current_position[0]][current_position[1]] = current_num
        current_num += 1            
        current_position[0] -= 1
    else:
        current_position[0] += 1
        current_position[1] -= 1
    for i in range(k - 1):
        grid[current_position[0]][current_position[1]] = current_num
        current_num += 1
        current_position[1] -= 1
    else:
        current_position[1] += 1
        current_position[0] += 1
    for i in range(k - 1):
        grid[current_position[0]][current_position[1]] = current_num
        current_num += 1
        current_position[0] += 1
    else:
        current_position[0] -= 1
        current_position[1] += 1
    for i in range(k - 1):
        grid[current_position[0]][current_position[1]] = current_num
        current_num += 1
        current_position[1] += 1
    else:
        current_position[1] -= 1

for i in range(n):
    for ii in range(n):
        if grid[i][ii] == num:
            result = abs(i - n // 2) + abs(ii - n // 2)

print(result)
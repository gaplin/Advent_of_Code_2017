def flip(grid: list, n: int) -> list:
    result = [['' for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for ii in range(n):
            result[i][ii] = grid[n - i - 1][ii]

    return result

def rotate(grid: list, n: int) -> list:
    result = [['' for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for ii in range(n):
            result[i][ii] = grid[n - ii - 1][i]

    return result

def get_all_rotations(grid: list, n: int):
    result = []
    for _ in range(4):
        grid = rotate(grid, n)
        result.append(grid)

    grid = flip(grid, n)
    for _ in range(4):
        grid = rotate(grid, n)
        result.append(grid)

    return result

def grid_to_str(grid: list) -> str:
    result = ''
    for row in grid:
        result += ''.join(row)

    return result

def enhance(grid: list, productions: dict, n: int) -> list:
    result = []
    k = 3
    if n % 2 == 0:
        k = 2

    for i in range(0, n, k):
        row = []
        for ii in range(0, n, k):
            key = grid_to_str([grid[y][ii: ii + k] for y in range(i, i + k)])
            row.append(productions[key])
        
        for ii in range(k + 1):
            row_reduced = []
            for k_grid in row:
                row_reduced += k_grid[ii]
            result.append(row_reduced)

    return result
            
input = open('input2.txt').read().splitlines()

productions = {}
for line in input:
    source, target = line.split(' => ')
    source = source.split('/')
    target = target.split('/')
    n = len(source)
    all_rotation = get_all_rotations(source, n)
    for grid in all_rotation:
        key = grid_to_str(grid)
        productions[key] = target

grid = [['.', '#', '.'], ['.', '.', '#'], ['#', '#', '#']]
size = 3
iterations = 18
for i in range(iterations):
    grid = enhance(grid, productions, size)
    size = len(grid)

count = 0
for row in grid:
    count += row.count('#')

print(count)
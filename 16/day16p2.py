def spin(programs: list, count: int, n: int) -> list:
    return programs[-count:] + programs[:n - count]

def exchange(programs: list, i: int, j: int) -> None:
    programs[i], programs[j] = programs[j], programs[i]

def partner(programs: list, a: str, b: str) -> None:
    i = programs.index(a)
    j = programs.index(b)
    programs[i], programs[j] = programs[j], programs[i]

def dance(programs: list, moves: list) -> list:
    for move in moves:
        if move[0] == 's':
            count = int(move[1:])
            programs = spin(programs, count, n)
        elif move[0] == 'x':
            i, j = [int(x) for x in move[1:].split('/')]
            exchange(programs, i, j)
        else:
            a, b = move[1:].split('/')
            partner(programs, a, b)

    return programs


moves = open('input2.txt').read().strip().split(',')

n = 16
programs = [chr(x + ord('a')) for x in range(n)]
orders = [tuple(programs)]
order_map = {tuple(programs): 0}

all_dances = 1000000000
for i in range(1, all_dances):
    programs = dance(programs, moves)
    key = tuple(programs)
    if key in order_map:
        cycle_start = order_map[key]
        cycle_length = i - cycle_start
        all_dances -= cycle_start
        all_dances %= cycle_length
        result = ''.join(orders[cycle_start + all_dances])
        break
    order_map[key] = i
    orders.append(key)

print(result)
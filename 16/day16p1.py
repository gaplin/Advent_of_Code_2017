def spin(programs: list, count: int, n: int) -> list:
    return programs[-count:] + programs[:n - count]

def exchange(programs: list, i: int, j: int) -> None:
    programs[i], programs[j] = programs[j], programs[i]

def partner(programs: list, a: str, b: str) -> None:
    i = programs.index(a)
    j = programs.index(b)
    programs[i], programs[j] = programs[j], programs[i]

moves = open('input2.txt').read().strip().split(',')

n = 16
programs = [chr(x + ord('a')) for x in range(n)]

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

print(''.join(programs))
diagram = open('input2.txt').read().splitlines()

n = len(diagram)
m = len(diagram[0])
no_turn = lambda x, y: (x, y)
left_turn = lambda x, y: (-y, x)
right_turn = lambda x, y: (y, -x)

current_position = [0, 0]
for i in range(m):
    if diagram[0][i] == '|':
        current_position[1] = i
        break

current_direction = (1, 0)
collected_letters = ''
while True:
    i, ii = current_position
    if diagram[i][ii].isalpha():
        collected_letters += diagram[i][ii]
    
    for turn in [no_turn, left_turn, right_turn]:
        di, dii = turn(*current_direction)
        new_i, new_ii = i + di, ii + dii
        if 0 <= new_i < n and 0 <= new_ii < m and diagram[new_i][new_ii] != ' ':
            current_position[0], current_position[1] = new_i, new_ii
            current_direction = (di, dii)
            break
    else:
        break

print(collected_letters)
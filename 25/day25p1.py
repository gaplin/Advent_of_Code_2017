import re

input = open('input2.txt').read().splitlines()

initial_state = input[0][-2]
checksum_after = int(re.findall(r'\d+', input[1])[0])

states = {}
current_state = None
for line in input[3:]:
    if line == '':
        states[current_state[0]] = current_state[1:]
        continue
    if line.startswith('In state'):
        current_state = [line[-2]]
    elif 'current value' in line:
        current_state.append([])
    elif 'Write' in line:
        current_state[-1].append(int(line[-2]))
    elif 'Move' in line:
        direction = line[:-1].split(' ')[-1]
        if direction == 'right':
            current_state[-1].append(1)
        else:
            current_state[-1].append(-1)
    else:
        current_state[-1].append(line[-2])
else:
    states[current_state[0]] = current_state[1:]

ones = set()
position = 0
current_state = states[initial_state]
while checksum_after > 0:
    branch = 0
    if position in ones:
        branch = 1
    
    if current_state[branch][0] == 0:
        if branch == 1:
            ones.remove(position)
    else:
        ones.add(position)
    
    position += current_state[branch][1]
    current_state = states[current_state[branch][2]]
    
    checksum_after -= 1

print(len(ones))
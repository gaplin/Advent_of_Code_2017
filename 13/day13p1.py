input = open('input2.txt').read().splitlines()

def get_scanner_position(depth: int, time: int) -> int:
    cycle_length = 2 * (depth - 1)
    pos = time % cycle_length
    if pos >= depth:
        pos = depth - (pos - depth + 1)

    return pos

layers = []
for line in input:
    layers.append([int(x) for x in line.split(': ')])

time, position, layer_id = 0, 0, 0
severity = 0
while position <= layers[-1][0]:
    if position < layers[layer_id][0]:
        time += 1
        position += 1
        continue

    scanner_position = get_scanner_position(layers[layer_id][1], time)
    if scanner_position == 0:
        severity += layers[layer_id][0] * layers[layer_id][1]
    position += 1
    layer_id += 1
    time += 1

print(severity)
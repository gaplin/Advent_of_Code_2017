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

def flawless_trip(layers: list, starting_time: int) -> int:
    time, position, layer_id = starting_time, 0, 0
    while position <= layers[-1][0]:
        if position < layers[layer_id][0]:
            time += 1
            position += 1
            continue

        scanner_position = get_scanner_position(layers[layer_id][1], time)
        if scanner_position == 0:
            return False
        position += 1
        layer_id += 1
        time += 1

    return True

starting_time = 0
while flawless_trip(layers, starting_time) != True:
    starting_time += 1

print(starting_time)
def generate_value(previous_value: int, mod: int, factor: int) -> int:
    return previous_value * factor % mod

def get_16_bits(value: int) -> int:
    mask = (1 << 16) - 1
    return value & mask

def proper_pair(A: int, B: int) -> bool:
    A_bits = get_16_bits(A)
    B_bits = get_16_bits(B)
    return A_bits == B_bits

def generate_values(previous_value: int, mod: int, factor: int, count: int, validity_mod: int, output: list) -> None:
    while count > 0:
        next_value = generate_value(previous_value, mod, factor)
        if next_value % validity_mod == 0:
            output.append(next_value)
            count -= 1
        previous_value = next_value

def get_comparison_result(A: list, B: list) -> int:
    matches = 0
    for a, b in zip(A, B):
        if proper_pair(a, b):
            matches += 1
            
    return matches

input = open('input2.txt').read().splitlines()
mod = 2147483647
factors = [16807, 48271]
previous_values = [0, 0]
to_compare = [[], []]
for idx, line in enumerate(input):
    num = int(line.split(' ')[-1])
    previous_values[idx] = num

count = 5000000
generate_values(previous_values[0], mod, factors[0], count, 4, to_compare[0])
generate_values(previous_values[1], mod, factors[1], count, 8, to_compare[1])

result = get_comparison_result(*to_compare)
print(result)
def generate_value(previous_value: int, mod: int, factor: int) -> int:
    return previous_value * factor % mod

def get_16_bits(value: int) -> int:
    mask = (1 << 16) - 1
    return value & mask


input = open('input2.txt').read().splitlines()
mod = 2147483647
factors = [16807, 48271]

generated_values = [[], []]
for idx, line in enumerate(input):
    num = int(line.split(' ')[-1])
    generated_values[idx].append(num)

for i in range(40000000):
    for ii in range(2):
        next_value = generate_value(generated_values[ii][-1], mod, factors[ii])
        generated_values[ii].append(next_value)
    
matches = 0
for a, b in zip(generated_values[0], generated_values[1]):
    a_bits = get_16_bits(a)
    b_bits = get_16_bits(b)
    if a_bits == b_bits:
        matches += 1

print(matches)
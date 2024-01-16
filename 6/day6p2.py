import re

banks = [int(x) for x in re.findall(r'\d+', open('input2.txt').read().strip())]
n = len(banks)

def redistribute(banks: list, n: int) -> None:
    max_b, max_idx = -1, -1

    for i in range(n):
        if banks[i] > max_b:
            max_b = banks[i]
            max_idx = i

    banks[max_idx] = 0
    i = (max_idx + 1) % n
    while max_b > 0:
        banks[i] += 1
        max_b -= 1
        i = (i + 1) % n

bank_cache = {tuple(banks): 0}

i = 0
result = 0
while True:
    redistribute(banks, n)
    i += 1
    key = tuple(banks)
    if key in bank_cache:
        result = i - bank_cache[key]
        break
    bank_cache[key] = i

print(result)
import re

input = open('input2.txt').read().splitlines()

result = 0
for line in input:
    nums = [int(x) for x in re.findall(r'\d+', line)]
    result += max(nums) - min(nums)

print(result)
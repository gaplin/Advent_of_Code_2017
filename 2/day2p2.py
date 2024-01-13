import re

input = open('input2.txt').read().splitlines()

result = 0
for line in input:
    nums = [int(x) for x in re.findall(r'\d+', line)]
    for idx1, num1 in enumerate(nums):
        for idx2, num2 in enumerate(nums):
            if idx1 != idx2 and num1 % num2 == 0:
                result += num1 // num2

print(result)
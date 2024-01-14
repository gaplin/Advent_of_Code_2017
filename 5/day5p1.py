nums = [int(x) for x in open('input2.txt').read().splitlines()]
n = len(nums)

current_position = 0

steps = 0
while 0 <= current_position < n:
    offset = nums[current_position]
    nums[current_position] += 1
    current_position += offset
    steps += 1

print(steps)
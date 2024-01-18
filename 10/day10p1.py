def reverse(nums: list, starting_position: int, length: int, n: int) -> None:
    if length <= 1:
        return
    
    stack = []
    for i in range(length):
        pos = (starting_position + i) % n
        stack.append(nums[pos])
    
    for i in range(length):
        pos = (starting_position + i) % n
        nums[pos] = stack.pop()


lengths = [int(x) for x in open('input2.txt').read().strip().split(',')]

n = 256
skip = 0
nums = [i for i in range(n)]
current_position = 0
for length in lengths:
    reverse(nums, current_position, length, n)
    current_position = (current_position + length + skip) % n
    skip += 1

print(nums[0] * nums[1])
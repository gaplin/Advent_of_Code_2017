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


lengths = [ord(x) for x in open('input2.txt').read().strip()]
lengths += [17, 31, 73, 47, 23]

n = 256
skip = 0
nums = [i for i in range(n)]
current_position = 0
for _ in range(64):
    for length in lengths:
        reverse(nums, current_position, length, n)
        current_position = (current_position + length + skip) % n
        skip += 1

groups = []
i = 0
while i < n:
    group = 0
    for _ in range(16):
        group ^= nums[i]
        i += 1
    groups.append(group)

result = ''
for group in groups:
    result += f'{group:0{2}x}' 

print(result)
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



def Hash(key: str) -> str:
    lengths = [ord(x) for x in key]
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

    return result

def get_row(hash: str) -> str:
    result = ''
    for char in hash:
        num = int(char, 16)
        result += f'{num:0{4}b}'

    return result 

hash_key = open('input2.txt').read().strip()
result = 0
for i in range(128):
    key = hash_key + '-' + str(i)
    H = Hash(key)
    row = get_row(H)
    result += row.count('1')

print(result)
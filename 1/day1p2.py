nums = [int(x) for x in open('input2.txt').read().strip()]
n = len(nums)

result = 0
incr = n >> 1
for i in range(n):
    if nums[i] == nums[(i + incr) % n]:
        result += nums[i]

print(result)
nums = [int(x) for x in open('input2.txt').read().strip()]
n = len(nums)

result = 0
for i in range(n):
    if nums[i] == nums[(i + 1) % n]:
        result += nums[i]

print(result)
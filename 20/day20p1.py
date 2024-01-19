import re

input = open('input2.txt')

particles = []

for line in input:
    nums = [int(x) for x in re.findall(r'[0-9-]+', line)]
    particles.append([nums[:3], nums[3:6], nums[6:]])

min_acc = 9999999999999
result = 0
for i, particle in enumerate(particles):
    accelerations = particle[2]
    total_acceleration = abs(accelerations[0]) + abs(accelerations[1]) + abs(accelerations[2])
    if total_acceleration < min_acc:
        result = i
        min_acc = total_acceleration

print(result)
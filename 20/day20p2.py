import re
from copy import deepcopy

def step(particles: dict) -> dict:
    new_places = {}
    result = {}
    for id, particle in particles.items():
        for i in range(3):
            particle[1][i] += particle[2][i]
            particle[0][i] += particle[1][i]
        
        new_position = tuple(particle[0])
        if new_position not in new_places:
            new_places[new_position] = []
        new_places[new_position].append(id)

    for ids in new_places.values():
        if len(ids) == 1:
            result[ids[0]] = particles[ids[0]]

    return result

def get_sorted_difs(particles: dict) -> list:
    result = []
    for id1, p1 in particles.items():
        for id2, p2 in particles.items():
            if id1 == id2:
                continue
            dist = abs(p1[0][0] - p2[0][0]) + abs(p1[0][1] - p2[0][1]) + abs(p1[0][2] - p2[0][2])
            result.append(dist)

    result.sort()
    return result

def any_lower_distance(A: list, B:list) -> bool:
    for a, b in zip(A, B):
        if a < b:
            return True
    
    return False

input = open('input2.txt')

particles = []

for line in input:
    nums = [int(x) for x in re.findall(r'[0-9-]+', line)]
    particles.append([nums[:3], nums[3:6], nums[6:]])

particles = {i: x for i, x in enumerate(particles)}
while True:
    new_particles = step(deepcopy(particles))
    if len(particles) == len(new_particles) and any_lower_distance(get_sorted_difs(new_particles), get_sorted_difs(particles)) == False:
        break

    particles = new_particles

print(len(particles))
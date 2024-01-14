input = open('input2.txt').read().splitlines()

result = 0
for line in input:
    words = line.split(' ')
    unique_words = set(words)
    if len(unique_words) == len(words):
        result += 1

print(result)
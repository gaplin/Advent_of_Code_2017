text = open('input2.txt').read().strip()
n = len(text)
level = 0
skip = False
garbage = False
result = 0
for char in text:
    if skip == True:
        skip = False
        continue
    if char == '!':
        skip = True
        continue

    if char == '{' and garbage == False:
        level += 1
        result += level
    elif char == '<' and garbage == False:
        garbage = True
    elif char == '}' and garbage == False:
        level -= 1
    elif char == '>':
        garbage = False
    
print(result) 
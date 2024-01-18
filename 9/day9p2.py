text = open('input2.txt').read().strip()
n = len(text)
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
    
    if char == '<' and garbage == False:
        garbage = True
    elif char == '>':
        garbage = False
    elif garbage == True:
        result += 1
    
print(result) 
step = int(open('input2.txt').read().strip())

zero = 0
result = 0
for i in range(1, 50000001):
    zero = (zero - step) % i
    if zero == i - 1:
        result = i

print(result)    
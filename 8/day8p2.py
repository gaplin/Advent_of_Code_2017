input = open('input2.txt').read().splitlines()

registers = {}
result = 0
for line in input:
    operation, condition = line.split(' if ')
    operation = operation.split(' ')
    operation[2] = int(operation[2])
    if operation[0] not in registers:
        registers[operation[0]] = 0
    
    condition = condition.split(' ')
    condition[2] = int(condition[2])
    if condition[0] not in registers:
        registers[condition[0]] = 0

    condition_satisfied = False
    if condition[1] == '>':
        condition_satisfied = registers[condition[0]] > condition[2]
    elif condition[1] == '<':
        condition_satisfied = registers[condition[0]] < condition[2]
    elif condition[1] == '>=':
        condition_satisfied = registers[condition[0]] >= condition[2]
    elif condition[1] == '==':
        condition_satisfied = registers[condition[0]] == condition[2]
    elif condition[1] == '<=':
        condition_satisfied = registers[condition[0]] <= condition[2]
    elif condition[1] == '!=':
        condition_satisfied = registers[condition[0]] != condition[2]

    if condition_satisfied == True:
        if operation[1] == 'inc':
            registers[operation[0]] += operation[2]
        else:
            registers[operation[0]] -= operation[2]
    max_register = max(registers.values())
    result = max(result, max_register)

print(result)
import string

def get_value(registers: dict, source: str) -> int:
    if source.isalpha():
        return registers[source]
    
    return int(source)

def jnz(program: list, X: str, Y: str) -> bool:
    X_value = get_value(program[0], X)
    Y_value = get_value(program[0], Y)
    if X_value != 0:
        program[1] += Y_value
        return True
    
    return False

def set(registers: dict, X: str, Y: str) -> None:
    registers[X] = get_value(registers, Y)

def sub(registers: dict, X: str, Y: str) -> None:
    registers[X] -= get_value(registers, Y)

def mul(registers: dict, X: str, Y: str) -> None:
    registers[X] *= get_value(registers, Y)

def count_muls(program: list) -> int:
    # program = [registers, ip, instructions]
    instructions = program[2]
    n = len(instructions)
    result = 0
    while 0 <= program[1] < n:
        instruction = instructions[program[1]].split(' ')
        if instruction[0] == 'jnz':
            if jnz(program, *instruction[1:]) == True:
                continue
        elif instruction[0] == 'set':
            set(program[0], *instruction[1:])
        elif instruction[0] == 'sub':
            sub(program[0], *instruction[1:])
        elif instruction[0] == 'mul':
            mul(program[0], *instruction[1:])
            result += 1
            
        program[1] += 1
    
    return result

instructions = open('input2.txt').read().splitlines()
program = [{x: 0 for x in string.ascii_lowercase}, 0, instructions]
result = count_muls(program)
print(result)
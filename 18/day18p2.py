import string
from queue import Queue

def get_value(registers: dict, source: str) -> int:
    if source.isalpha():
        return registers[source]
    
    return int(source)

def snd(registers: dict, X: str, Q: Queue) -> int:
    Q.put(get_value(registers, X))

def rcv(registers: dict, X: str, Q: Queue) -> bool:
    if Q.empty() == True:
        return False
    
    registers[X] = Q.get()
    return True

def jgz(program: list, X: str, Y: str) -> bool:
    X_value = get_value(program[0], X)
    Y_value = get_value(program[0], Y)
    if X_value > 0:
        program[1] += Y_value
        return True
    
    return False

def set(registers: dict, X: str, Y: str) -> None:
    registers[X] = get_value(registers, Y)

def add(registers: dict, X: str, Y: str) -> None:
    registers[X] += get_value(registers, Y)

def mul(registers: dict, X: str, Y: str) -> None:
    registers[X] *= get_value(registers, Y)

def mod(registers: dict, X: str, Y: str) -> None:
    registers[X] %= get_value(registers, Y)

def can_continue(program: list, n: int) -> bool:
    if program[1] < 0 or program[1] >= n:
        return False
    
    if program[4] == True and program[3].empty() == True:
        return False
    
    return True

def get_message_count_of_program1(programs: list) -> int:
    # program = [registers, ip, instructions, Q, receiving]
    instructions = programs[0][2]
    n = len(instructions)
    result = 0
    while True:
        moves = 0
        for i in range(2):
            program = programs[i]
            if can_continue(program, n) == False:
                break
            moves += 1
            instruction = instructions[program[1]].split(' ')
            if instruction[0] == 'jgz':
                if jgz(program, *instruction[1:]) == True:
                    continue
            elif instruction[0] == 'snd':
                if i == 1:
                    result += 1
                snd(program[0], instruction[1], programs[1 - i][3])
            elif instruction[0] == 'rcv':
                if rcv(program[0], instruction[1], program[3]) == False:
                    program[4] = True
                    continue
                else:
                    program[4] = False
            elif instruction[0] == 'set':
                set(program[0], *instruction[1:])
            elif instruction[0] == 'add':
                add(program[0], *instruction[1:])
            elif instruction[0] == 'mul':
                mul(program[0], *instruction[1:])
            elif instruction[0] == 'mod':
                mod(program[0], *instruction[1:])
        
            program[1] += 1
        if moves == 0:
            break

    return result

instructions = open('input2.txt').read().splitlines()
program0 = [{x: 0 for x in string.ascii_lowercase}, 0, instructions, Queue(), False]
program1 = [{x: 0 for x in string.ascii_lowercase}, 0, instructions, Queue(), False]
program0[0]['p'] = 0
program1[0]['p'] = 1

programs = [program0, program1]

result = get_message_count_of_program1(programs)
print(result)
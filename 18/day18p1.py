import string

def get_value(registers: dict, source: str) -> int:
    if source.isalpha():
        return registers[source]
    
    return int(source)

def snd(registers: dict, X: str) -> int:
    return get_value(registers, X)

def rcv(registers: dict, X: str, last_sound: int) -> int:
    if get_value(registers, X) != 0:
        return last_sound
    
    return None

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


def play_until_rcv(program: list) -> int:
    # program = [registers, ip, instructions]
    last_sound = None
    instructions = program[2]
    n = len(instructions)
    while 0 <= program[1] < n:
        instruction = instructions[program[1]].split(' ')
        if instruction[0] == 'jgz':
            if jgz(program, *instruction[1:]) == True:
                continue
        elif instruction[0] == 'snd':
            last_sound = snd(program[0], instruction[1])
        elif instruction[0] == 'rcv':
            if rcv(program[0], instruction[1], last_sound) != None:
                return last_sound
        elif instruction[0] == 'set':
            set(program[0], *instruction[1:])
        elif instruction[0] == 'add':
            add(program[0], *instruction[1:])
        elif instruction[0] == 'mul':
            mul(program[0], *instruction[1:])
        elif instruction[0] == 'mod':
            mod(program[0], *instruction[1:])
        
        program[1] += 1

instructions = open('input2.txt').read().splitlines()
program = [{x: 0 for x in string.ascii_lowercase}, 0, instructions]
result = play_until_rcv(program)
print(result)
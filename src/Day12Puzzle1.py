instructions = """cpy 1 a
cpy 1 b
cpy 26 d
jnz c 2
jnz 1 5
cpy 7 c
inc d
dec c
jnz c -2
cpy a c
inc a
dec b
jnz b -2
cpy c b
dec d
jnz d -6
cpy 16 c
cpy 17 d
inc a
dec d
jnz d -2
dec c
jnz c -5"""
registers = {
    'a': 0,
    'b': 0,
    'c': 0,
    'd': 0
}
instructions_array = instructions.split('\n')

for instruction_index in range(len(instructions_array)):
    instruction_parts = instructions_array[instruction_index].split(" ")
    if instruction_parts[0] == 'cpy':
        try:  # if we can convert it to an int, the instruction is a plain number
            number_to_copy_into_register = int(instruction_parts[1])
        except:  # if not, it must be pointing to a register
            number_to_copy_into_register = registers[instruction_parts[1]]
        registers[instruction_parts[2]] = number_to_copy_into_register
    elif instruction_parts[0] == 'jnz':
        try:  # if we can convert it to an int, the instruction is a plain number
            number_to_compare = int(instruction_parts[1])
        except:  # if not, it must be pointing to a register
            number_to_compare = registers[instruction_parts[1]]

        if number_to_compare > 0:
            instruction_index += int(instruction_parts[2])
    elif instruction_parts[0] == 'inc':
        registers[instruction_parts[1]] += 1
    elif instruction_parts[0] == 'dec':
        registers[instruction_parts[1]] -= 1
    else:
        print 'instruction not found'

print 'end:', registers
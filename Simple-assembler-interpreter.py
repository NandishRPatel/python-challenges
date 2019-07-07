def simple_assembler(program):
    final_dict = {}
    i = 0
    while i < len(program):
    	instruction = program[i] + " 0"
    	command, key, value = instruction.split()[:3]
    	if command == 'mov':final_dict[key] = final_dict[value] if value in final_dict else int(value)
    	
    	if command == "inc":final_dict[key] += 1
    	
    	if command == "jnz" and (final_dict[key] if key in final_dict else int(key)):i += int(value) - 1
    	
    	if command == "dec": final_dict[key] -= 1
    	
    	i += 1
    return final_dict

code = '''\
mov c 12
mov b 0
mov a 200x
dec a
inc b
jnz a -2
dec c
mov a b
jnz c -5
jnz 0 1
mov c a'''

print(simple_assembler(['mov a 1', 'mov b 1', 'mov c 0', 'mov d 26', 'jnz c 2', 'jnz 1 5', 'mov c 7', 'inc d', 'dec c', 'jnz c -2', 'mov c a', 'inc a', 'dec b', 'jnz b -2', 'mov b c', 'dec d', 'jnz d -6', 'mov c 18', 'mov d 11', 'inc a', 'dec d', 'jnz d -2', 'dec c', 'jnz c -5']))
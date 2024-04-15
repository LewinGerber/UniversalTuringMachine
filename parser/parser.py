PROGRAM_TAPE_SEPARATOR = "111"
STATE_SEPARATOR = "11"
GENERAL_SEPARATOR = "1"

whole_input = "10101000101001101001010010011000101000010100110001001010010011000010100001010011000010010000100100110000100010010001001111001"

def parse(input: str):
    program, tape = input.split(PROGRAM_TAPE_SEPARATOR, 1)

    states = {}
    for line in program.split(STATE_SEPARATOR):
        element = list(filter(None, line.split(GENERAL_SEPARATOR)))
        states[str(len(element[0])) + str(len(element[1]))] = (len(element[2]), len(element[3]), len(element[4]))
    
    return states, list(tape)

print(parse(whole_input))
PROGRAM_TAPE_SEPARATOR = "111"
STATE_SEPARATOR = "11"
GENERAL_SEPARATOR = "1"

whole_input = "10101000101001101001010010011000101000010100110001001010010011000010100001010011000010010000100100110000100010010001001111001"

# Create a map with a key which is concatenated: STATE + TAPE ELEMENT (e.g. Key 11 means Q1 reading 0, 12 means Q1 reading 1)
# the maps value is a tuple consisting of 1. new state, 2. what is writte to tape, 3. which direction to move
def parse(input: str):
    program, tape = input.split(PROGRAM_TAPE_SEPARATOR, 1)

    states = {}
    for line in program.split(STATE_SEPARATOR):
        element = list(filter(None, line.split(GENERAL_SEPARATOR)))
        states[f"{len(element[0])}{len(element[1])}"] = (len(element[2]), len(element[3]), len(element[4]))
    
    return states, list(tape)

print(parse(whole_input))
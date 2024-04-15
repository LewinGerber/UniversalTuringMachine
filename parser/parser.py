STATE_SEPARATOR = "11"
GENERAL_SEPARATOR = "1"

input = "1010100010100110100101001001100010100001010011000100101001001100001010000101001100001001000010010011000010001001000100"
tape = list("1001")
states = {}

for line in input.split(STATE_SEPARATOR):
    element = list(filter(None, line.split(GENERAL_SEPARATOR)))
    states[str(len(element[0])) + str(len(element[1]))] = (len(element[2]), len(element[3]), len(element[4]))


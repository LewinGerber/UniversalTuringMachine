import argparse
from tm_parser import parse

def calculate(states, tape: list):
    current_state = 1 # starting state is defined as Q1
    current_index = 0

    while current_state != 2:
        value_on_tape = read_from_tape(tape, current_index)
        next_state, element_on_tape, direction = states[f"{current_state}{value_on_tape}"]

        # append_to_tape(element_on_tape, current_index)
        tape[current_index] = element_on_tape

        current_state = next_state
        if direction == 2:
            current_index += 1
        elif direction ==1:
            current_index -= 1
    
    print(tape)

def append_to_tape(element_to_append, index):
    pass

def read_from_tape(tape, index):
    if index < 0 or index >= len(tape):
        return 3
    return tape[index]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input')
    args = parser.parse_args()
    calculate(*parse(args.input))

if __name__ == "__main__":
    main()
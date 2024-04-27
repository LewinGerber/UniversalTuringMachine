import arrr
from pyscript import document
import argparse
from tm_parser import parse

def calculate(states, tape: list):
    current_state = 1 # starting state is defined as Q1
    current_index = 0

    print(states)

    while current_state != 2:
        value_on_tape = read_from_tape_or_space(tape, current_index)
        print(f"Current state: {current_state}, Reading value: {value_on_tape}, Tape Position: {current_index}")
        next_state, element_on_tape, direction = states[f"{current_state}{value_on_tape}"]

        if current_index > (len(tape) - 1):
            tape.append(element_on_tape)
        elif current_index < 0:
            tape.insert(0, element_on_tape)
            current_index += 1
        else:
            tape[current_index] = element_on_tape

        current_state = next_state
        if direction == 2:
            current_index += 1
        elif direction ==1:
            current_index -= 1
    
    print(f"Ended in state: {current_state}")
    print(tape)

def read_from_tape_or_space(tape, index):
    if index < 0 or index >= len(tape):
        return 3
    return int(tape[index]) + 1

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input')
    args = parser.parse_args()
    calculate(*parse(args.input))

def py_script_hook(event):
    input = document.querySelector("#machine-input-code").value
    calculate(*parse(input))

#if __name__ == "__main__":
#    main()
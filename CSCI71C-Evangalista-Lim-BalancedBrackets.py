import io 
import sys
import contextlib

# Checks if the given expression has balanced brackets using the PDA simulation
def is_balanced(expression):
    state = "q0" # Initial state 
    stack = ["Z"] # Stack initialized with bottom marker
    position = 0 # Tracks character position  
    extra = False # Flag for extra characters
    displayExpression = expression # Keeps the original expression for output
    accepted = False # Tracks if the expression is accepted

    # Prints an error when a mismatch occurs at a specific position
    def pos_error_message():
        print(f"Invalid string. Failed at position {position}.")
        print(f"Remaining unprocessed input string: {expression}")

    # Prints an error if final state is not accepting
    def state_error_message():
        print(f"Invalid string. {state} is not a final state.")

    # Prints success message if expression is valid and accepted
    def success_message():
        print(f"{state} is a final state.")
        print(f"{displayExpression} is valid and has balanced brackets.")

    # Shows the current ID
    def process_message():
        stringStack = "".join(stack)
        print(f"ID: ({state}, {expression}, {stringStack})")

    # Shows the current expression that is processing
    print(f"Processing {expression}")

    # PDA main loop
    while expression != "E" and stack:
        position += 1

        if not expression:
            expression = "E" # Replace empty input with E to trigger final check

        process_message()

        # Start state: expecting opening '!'
        if state == "q0":
            if expression[0] == "!":
                stack.insert(0, "!")
                state = "q1"
                expression = expression[1:]
            else:
                pos_error_message()
                break

        # Main parsing state            
        elif state == "q1":
            if expression[0] == "x":
                expression = expression[1:]

            # Opening brackets: push to stack
            elif expression[0] == "<":
                stack.insert(0, "<")
                expression = expression[1:]
            elif expression[0] == "{":
                stack.insert(0, "{")
                expression = expression[1:]
            elif expression[0] == "[":
                stack.insert(0, "[")
                expression = expression[1:]
            elif expression[0] == "(":
                stack.insert(0, "(")
                expression = expression[1:]
            
            # Closing brackets: check top of stack and pop if it matches
            elif expression[0] == ">":
                if stack[0] == "<":
                    stack.pop(0)
                    expression = expression[1:]
                else:
                    pos_error_message()
                    break
            elif expression[0] == "}":
                if stack[0] == "{":
                    stack.pop(0)
                    expression = expression[1:]
                else:
                    pos_error_message()
                    break
            elif expression[0] == "]":
                if stack[0] == "[":
                    stack.pop(0)
                    expression = expression[1:]
                else:
                    pos_error_message()
                    break
            elif expression[0] == ")":
                if stack[0] == "(":
                    stack.pop(0)
                    expression = expression[1:]
                else:
                    pos_error_message()
                    break
        
            # Must match opening '!'
            elif expression[0] == "!":
                if stack[0] == "!":
                    stack.pop(0)
                    state = "q2"
                    expression = expression[1:]
                else:
                    pos_error_message()
                    break
    
            # Reached E prematurely or invalid character
            elif expression[0] == "E":
                state_error_message()
                break
            else:
                pos_error_message()
                break

        # Final state: ensure stack is only bottom marker left             
        elif state == "q2":
            if expression != "E":
                pos_error_message()
                extra = True
                break
            else:
                stack.pop(0)

    # If reached final state with no extra input, accept
    if state == "q2" and not extra:
        success_message()
        accepted = True
    
    return accepted

# Evaluates number of x's based on nested bracket operations
def evaluate(expression):
    xStack = [0] # Stack to manage bracket-specific x counts
    
    while expression:
        if expression[0] == "x":
            xStack[0] += 1
            expression = expression[1:]

         # Opening any bracket: push new x counter
        elif expression[0] == "<":
            xStack.insert(0, 0)
            expression = expression[1:]
        elif expression[0] == "{":
            xStack.insert(0, 0)
            expression = expression[1:]
        elif expression[0] == "[":
            xStack.insert(0, 0)
            expression = expression[1:]
        elif expression[0] == "(":
            xStack.insert(0, 0)
            expression = expression[1:]

        # Closing > bracket: double current, add to outer
        elif expression[0] == ">":
            xStack[0] *= 2
            xStack[1] += xStack[0]
            xStack.pop(0)
            expression = expression[1:]
        
        # Closing } bracket: add 1 to current, then add to outer
        elif expression[0] == "}":
            xStack[0] += 1
            xStack[1] += xStack[0]
            xStack.pop(0)
            expression = expression[1:]

        # Closing ] bracket: discard current
        elif expression[0] == "]":
            xStack.pop(0)
            expression = expression[1:]

        # Closing ): subtract 1 from current (min 0), add to outer
        elif expression[0] == ")":
            xStack[0] -= 1 if xStack[0] > 0 else 0
            xStack[1] += xStack[0]
            xStack.pop(0)
            expression = expression[1:]
        
         # Ignore any unrecognized characters
        else:
            expression = expression[1:]
    
    return xStack[0]

# Runs is_balanced() on each line of input file and prints trace
def main1(input_file):
    with open(input_file, 'r') as file:
        for line in file:
            expression = line.strip()
            if expression:  
                if is_balanced(expression):
                    inner_expr = expression[1:-1]  # Extract content between ! and !
                print() # Print a /n for line separation

# Evaluates only valid expressions and prints the result
def main2(input_file):
    with open(input_file, 'r') as file:
        for line in file:
            expression = line.strip()
            if expression:
                with contextlib.redirect_stdout(io.StringIO()):  # Silence PDA trace output to check validity of string
                    valid = is_balanced(expression)
                if valid:
                    result = evaluate(expression[1:-1]) # Extract content between ! and !
                    print(f"{expression} - Resulting number of x's: {result}")
                else:
                    print(f"{expression} - Invalid string.")

if __name__ == "__main__":
    input_file = "input2.txt" # name of input file
    main1(input_file)
    main2(input_file)

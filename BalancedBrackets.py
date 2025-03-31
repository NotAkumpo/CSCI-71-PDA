def is_balanced(expression):
    state = "q0"
    stack = [ "Z" ]
    position = 1
    displayExpression = expression

    print(f"Processing {expression}")

    while (state != "q2" or expression):
        process_message(state, expression, stack)
        if state == "q0":
            if expression[0] == "!":
                stack.append("!")
                state = "q1"
                expression = expression[1:]
            else:
                pos_error_message()
                break            
        elif state == "q1":
            if expression[0] == "x":
                expression = expression[1:]
            elif expression[0] == "<":
                stack.append("<")
                expression = expression[1:]
            elif expression[0] == "{":
                stack.append("{")
                expression = expression[1:]
            elif expression[0] == "[":
                stack.append("[")
                expression = expression[1:]
            elif expression[0] == "(":
                stack.append("(")
                expression = expression[1:]
            elif expression[0] == ">":
                if stack[0] == "<":
                    stack.pop()
                    expression = expression[1:]
                else:
                    pos_error_message()
                    break
            elif expression[0] == "}":
                if stack[0] == "{":
                    stack.pop()
                    expression = expression[1:]
                else:
                    pos_error_message()
                    break
            elif expression[0] == "]":
                if stack[0] == "[":
                    stack.pop()
                    expression = expression[1:]
                else:
                    pos_error_message()
                    break
            elif expression[0] == ")":
                if stack[0] == "(":
                    stack.pop()
                    expression = expression[1:]
                else:
                    pos_error_message()
                    break
            elif expression[0] == "!":
                if stack[0] == "!":
                    stack.pop()
                    state = "q2"
                    expression = expression[1:]
                else:
                    pos_error_message()
                    break
            else:
                pos_error_message()
                break
                        
        elif state == "q2":
            pass
    

    def pos_error_message():
        print(f"Invalid string. Failed at position {position}")
        print(f"Remaining unprocessed input string: {expression}")

    def state_error_message():
        print(f"Invalid string. {state} is not a final state.")

    def success_message():
        print("{displayExpression} is valid and has balanced brackets.")

    def process_message(state, expression, stack):
        stringStack = "".join(stack)
        print(f"ID: ({state}, {expression}, {stringStack})")

# exp = input("Enter the expression: ")
# is_balanced("john")
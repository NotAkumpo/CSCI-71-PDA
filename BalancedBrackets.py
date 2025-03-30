def is_balanced(expression):
    state = "q0"
    stack = [ "Z" ]
    position = 0
    displayExpression = expression

    while (state != "q2" or expression):
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
                    state_error_message()
                    break
            elif expression[0] == "}":
                if stack[0] == "{":
                    stack.pop()
                    expression = expression[1:]
                else:
                    state_error_message()
                    break
            elif expression[0] == "]":
                if stack[0] == "[":
                    stack.pop()
                    expression = expression[1:]
                else:
                    state_error_message()
                    break
            elif expression[0] == ")":
                if stack[0] == "(":
                    stack.pop()
                    expression = expression[1:]
                else:
                    state_error_message()
                    break
            elif expression[0] == "!":
                if stack[0] == "!":
                    stack.pop()
                    expression = expression[1:]
                    if expression:
                        
        elif state == "q2":
            pass

    def pos_error_message():
        print(f"Invalid string. Failed at position {position}")

    def state_error_message():
        print(f"Invalid string. {state} is not a final state.")

    def success_message():
        print("{displayExpression} is valid and has balanced brackets.")

# exp = input("Enter the expression: ")
# is_balanced("john")
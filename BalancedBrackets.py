def is_balanced(expression):
    state = "q0"
    stack = ["Z"]
    position = 0
    extra = False
    displayExpression = expression

    def pos_error_message():
        print(f"Invalid string. Failed at position {position}.")
        print(f"Remaining unprocessed input string: {expression}")

    def state_error_message():
        print(f"Invalid string. {state} is not a final state.")

    def success_message():
        print(f"{state} is a final state.")
        print(f"{displayExpression} is valid and has balanced brackets.")

    def process_message():
        stringStack = "".join(stack)
        print(f"ID: ({state}, {expression}, {stringStack})")

    print(f"Processing {expression}")

    while expression != "E" and stack:
        position += 1

        if not expression:
            expression = "E"

        process_message()
        if state == "q0":
            if expression[0] == "!":
                stack.insert(0, "!")
                state = "q1"
                expression = expression[1:]
            else:
                pos_error_message()
                break            
        elif state == "q1":
            if expression[0] == "x":
                expression = expression[1:]
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
            elif expression[0] == "!":
                if stack[0] == "!":
                    stack.pop(0)
                    state = "q2"
                    expression = expression[1:]
                else:
                    pos_error_message()
                    break
            elif expression[0] == "E":
                state_error_message()
                break
            else:
                pos_error_message()
                break
                        
        elif state == "q2":
            if expression != "E":
                pos_error_message()
                extra = True
                break
            else:
                stack.pop(0)

    if state == "q2" and not extra:
        success_message()


def evaluate(expression):
    xStack = [0]
    
    while expression:
        if expression[0] == "x":
            xStack[0] += 1
            expression = expression[1:]
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
        elif expression[0] == ">":
            xStack[0] *= 2
            xStack[1] += xStack[0]
            xStack.pop(0)
            expression = expression[1:]
        elif expression[0] == "}":
            xStack[0] += 1
            xStack[1] += xStack[0]
            xStack.pop(0)
            expression = expression[1:]
        elif expression[0] == "]":
            xStack.pop(0)
            expression = expression[1:]
        elif expression[0] == ")":
            xStack[0] -= 1 if xStack[0] > 0 else 0
            xStack[1] += xStack[0]
            xStack.pop(0)
            expression = expression[1:]
        else:
            expression = expression[1:]
    
    print(f"Resulting number of x's: {xStack[0]}")





# exp = input("Enter the expression: ")
# is_balanced("john")

# exp = "i"
# exp = exp[1:]

# if (exp):
#     print(exp)
# else:
#     print("Fail")

# is_balanced("!xx[x({xx})[xxx]x]<xxx>x!")
# is_balanced("![<]>!")
# is_balanced("![]")
# is_balanced("!<a{[()]}a>!")
# is_balanced("([]){}")
# is_balanced("!<x{[()]}x>!")

evaluate("!<x{[()]}x>!")

# array = ["john", "alice"]
# array.insert(0, "bob")
# print(array[0])

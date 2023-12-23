num1 = float(input("Enter a number: ")) # gets a number
num2 = float(input("Enter a number: ")) # gets a number
operator = input("Operation: ") # asks for an operation

def calculate():
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    else:
        return "Not defined."

print(calculate()) # prints the final result



from art import logo

# Addition function
def add(n1, n2):
    return n1 + n2

# Subtraction function
def subtract(n1, n2):
    return n1 - n2

# Multiplication function
def multiply(n1, n2): 
    return n1 * n2

# Division function
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        # Ask if the user wants to continue calculating with the answer
        continue_calculation = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation, or 'e' to exit: ")
        if continue_calculation == "y":
            num1 = answer
        elif continue_calculation == "e":
            print("Exiting the calculator. Goodbye!")
            should_continue = False
            exit()
        else:
            should_continue = False
            calculator()
calculator()
# This code is a simple calculator that performs basic arithmetic operations (addition, subtraction, multiplication, and division).

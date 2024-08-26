def add(n1, n2):
    return n1 + n2

# TODO: Write out the other 3 functions - subtract, multiply and divide.
def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


# TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# TODO: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.
op = "*"
print(operations[op](4, 8))




# first_number = input("What's the first number?: ")
# operation = input("+\n-\n*\n/\nPick an operation: ")
# second_number = input("What's the second number?")
#
#
# if operation == "+":
#     answer = add(first_number, second_number)
#     print(f"{first_number} {operation} {second_number} = {answer}")
# elif operation == "-":
#     answer = subtract(first_number, second_number)
#     print(f"{first_number} {operation} {second_number} = {answer}")
# elif operation == "*":
#     answer = multiply(first_number, second_number)
#     print(f"{first_number} {operation} {second_number} = {answer}")
# elif operation == "/":
#     answer = divide(first_number, second_number)
#     print(f"{first_number} {operation} {second_number} = {answer}")

import art
print(art.logo)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

keep_result = True


def calc():
    operation = input("+\n-\n*\n/\nPick an operation: ")
    second_number = float(input("What's the second number?: "))
    answer = operations[operation](first_number, second_number)
    print(f"{first_number} {operation} {second_number} = {answer}")
    return answer

while 1 > 0:
    first_number = float(input("What's the first number?: "))
    answer = calc()
    continue_or_not = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()

    while keep_result:
        if continue_or_not == 'y':
            first_number = answer
            answer = calc()
            continue_or_not = input(
                f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
        elif continue_or_not == 'n':
            keep_result = False

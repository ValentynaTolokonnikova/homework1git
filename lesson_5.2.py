# Calculator_2

while True:
    first_number = input("Type first number:")
    operation = input("Input operation:+,-,*, or /")
    second_number = input("Type second number:")

    if not first_number.isdigit() or not second_number.isdigit() or operation not in ("+", "-", "*", "/"):
        print("Invalid input")
        continue
    first_number = float(first_number)
    second_number = float(second_number)
    result = 0

    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    elif operation == "/":
        if second_number != 0:
            result = first_number / second_number
        else:
            print("Zero Division Error")

    print(result)

    cont = input("To continue press Yes or No")
    if cont.lower() != "y":
        print("Good Bye")
        break

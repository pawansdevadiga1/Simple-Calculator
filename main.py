# Simple calculator
num1 = int(input("Enter your number: "))
num2 = int(input("Enter your second number: "))
operation = input("Choose your operation(+,-,*,/): ")

match operation:
    case '+':
        print("The result is",num1 + num2)
    case '-':
        print("The result is",num1 - num2)
    case '*':
        print("The result is",num1 * num2)
    case '/':
        print("The result is",num1 / num2)
    case _:
        print(operation)


# Simple Calculator

This is a Python program that implements a simple calculator. It takes two numbers and an arithmetic operation as input from the user and prints the result of the operation.

## Detailed Explanation

1. **Getting User Input:**
    ```python
    num1 = int(input("Enter your number: "))
    num2 = int(input("Enter your second number: "))
    operation = input("Choose your operation(+,-,*,/): ")
    ```
    These lines prompt the user to enter two numbers (`num1` and `num2`) and choose an arithmetic operation (`operation`). The `input` function captures the user's input, and `int` converts the input to an integer.

2. **Performing the Chosen Operation:**
    ```python
    match operation:
        case '+':
            print("The result is", num1 + num2)
        case '-':
            print("The result is", num1 - num2)
        case '*':
            print("The result is", num1 * num2)
        case '/':
            print("The result is", num1 / num2)
        case _:
            print(operation)
    ```
    The `match` statement is used to perform pattern matching on the `operation` input. Depending on the value of `operation`, one of the following cases will be executed:
    - **`case '+'`:** If the operation is addition, the program prints the sum of `num1` and `num2`.
    - **`case '-'`:** If the operation is subtraction, the program prints the difference between `num1` and `num2`.
    - **`case '*'`:** If the operation is multiplication, the program prints the product of `num1` and `num2`.
    - **`case '/'`:** If the operation is division, the program prints the quotient of `num1` divided by `num2`.
    - **`case _`:** This is the default case, which will execute if none of the specified operations match. It simply prints the `operation` string, which is not a valid arithmetic operator in this context.

## How to Run the Program

1. Save the code in a file with a `.py` extension, for example, `main.py`.
2. Run the file using Python:
    ```bash
    python main.py
    ```
3. Follow the prompts to enter the first number, the second number, and the desired operation.
4. The program will display the result of the chosen operation.

## Example Interaction
```bash
Enter your number: 10
Enter your second number: 5
Choose your operation(+,-,*,/): *
The result is 50
```

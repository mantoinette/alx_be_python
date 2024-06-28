
# Prompt user for input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

# Perform the calculation based on the chosen operation
match operation:
  case "+":
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is {result}")
  case "-":
    result = num1 - num2
    print(f"The subtraction of {num1} and {num2} is {result}")
  case "*":
    result = num1 * num2
    print(f"The multiplication of {num1} and {num2} is {result}")
  case "/":
    if num2 == 0:
        print("Division by zero is not allowed")
    else:
        result = num1 / num2
        print(f"The division of {num1} and {num2} is {result}")
  case _:
    print("Invalid operation. Please choose from '+', '-', '*', '/'.")


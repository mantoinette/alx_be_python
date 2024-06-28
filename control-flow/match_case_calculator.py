def main():
# Prompt user for input
 num1 = float(input("Enter the first number: "))
 num2 = float(input("Enter the second number: "))
 operation = input("Choose the operation (+, -, *, /): ")

# Perform the calculation based on the chosen operation
 
 match operation:
  case "+":
    result = num1 + num2
    print(f"the result is {result}")
  case "-":
    result = num1 - num2
    print(f" the result is {result}")
  case "*":
    result = num1 * num2
    print(f"the result is {result}")
  case "/":
    if num2 == 0:
        print("Division by zero is not allowed")
    else:
        result = num1 / num2
        print(f"the result is {result}")
  case _:
    print("Invalid operation. Please choose from '+', '-', '*', '/'.")
if __name__ == "__main__":
     main()


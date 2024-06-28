number = float(input("Enter a number to see its multiplication table: "))

# Iterate from 1 to 10 and print the multiplication table
for i in range(1, 11):
    result = number * i
    print(f"{number} * {i} = {result}")


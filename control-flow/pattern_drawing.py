user = int(input("Enter the size of the pattern: "))
i = 1
while i <= user:
    print("*" * user, end="")  # Print '*' repeated 'user' times for each row without newline
    i += 1

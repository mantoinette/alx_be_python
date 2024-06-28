# Ask the user to input the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
i = 1

# Loop through each row
while i <= size:
    # Loop through each column in the current row
    for j in range(size):
        # Print an asterisk without a newline
        print("*", end="")
    # Print a newline character to move to the next row
    print()
    # Increment the row counter
    i += 1

# Python program to print a star pattern
# based on the number of rows entered by the user

# Get number of rows from user
n = int(input("Enter the number of rows: "))

# Outer loop for rows
for i in range(1, n + 1):
    # Inner loop for columns
    for j in range(i):
        print("*", end=" ")
    # New line after each row
    print()

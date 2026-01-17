# Python program to check if a number is a palindrome

# Take input from the user
number = int(input("Enter your number: "))

# Store the original number for comparison
original_number = number

# Variable to store the reversed number
reversed_number = 0

# Reverse the number using a while loop
while number > 0:
    digit = number % 10          # Get last digit
    reversed_number = reversed_number * 10 + digit
    number //= 10                # Remove last digit

# Check if original number and reversed number are equal
if original_number == reversed_number:
    print(f"{original_number} is a palindrome")
else:
    print(f"{original_number} is not a palindrome")

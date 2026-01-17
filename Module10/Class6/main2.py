# Python program to print numbers from 1 to 3000
# that are both PRIME and PALINDROME

# Loop through numbers from 1 to 3000
for num in range(1, 3001):

    # Step 1: Check if number is PRIME
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    # Prime numbers have exactly 2 factors
    if count == 2:

        # Step 2: Check if number is PALINDROME
        temp = num
        reverse = 0

        while temp > 0:
            digit = temp % 10
            reverse = reverse * 10 + digit
            temp //= 10

        # If prime number is also palindrome, print it
        if reverse == num:
            print(num)

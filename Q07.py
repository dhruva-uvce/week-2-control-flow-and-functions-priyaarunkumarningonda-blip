# Q07. Reverse a Number (while loop)
#
# Ask the user for a positive integer.
# Print the reverse of the number using a while loop.
#
# Sample Input 1:   Enter a number: 1234
# Sample Output 1:  Reversed: 4321
#
# Sample Input 2:   Enter a number: 5000
# Sample Output 2:  Reversed: 5

# --- YOUR CODE HERE ---
number = int(input("Enter a number: "))
reversed_num = 0
original_num = number

while number > 0:
    digit = number % 10
    reversed_num = reversed_num * 10 + digit
    number //= 10

print(f"Reversed: {reversed_num}")

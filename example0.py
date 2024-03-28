#write a program to print a ternary operator that checks if the number is even or odd. If the number is even, it should print "Even" and if the number is odd, it should print "Odd". The program should use the ternary operator to achieve this. The program should take an integer as input and print the result accordingly. If the input is not an integer, it should print "Invalid input" and exit.
#
# Example
# Input
# 5
# Output
# Odd
# Input
# 10
# Output    
# Even
# Input
# 7.5
# Output
# Invalid input
#
# Hints
# Use the ternary operator to check if the number is even or odd. The ternary operator has the following syntax:
#
# <expression1> if <condition> else <expression2>
#

# Solution
# This program checks if the input number is even or odd using the ternary operator.
import sys
try:
    number = int(input())
except ValueError:
    print("Invalid input")
    sys.exit()
result = "Even" if number % 2 == 0 else "Odd"
print(result)


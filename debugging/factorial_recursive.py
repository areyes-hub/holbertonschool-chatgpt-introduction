#!/usr/bin/python3
import sys

# Function Description:
# The `factorial` function computes the factorial of a given number n.
# It uses recursion to multiply n by the factorial of (n-1) until n equals 0.
# The base case for the recursion is when n == 0, which returns 1, as 0! is 1 by definition.

# Parameters:
# n (int): The number for which the factorial is to be calculated. 
# n must be a non-negative integer, as factorial is only defined for non-negative integers.

# Returns:
# int: The factorial of the input number n. 
# If n is 0, the function returns 1. For any other non-negative integer n, it returns the product of all integers from 1 to n.

def factorial(n):
    if n == 0:  # Base case: factorial of 0 is 1
        return 1
    else:
        return n * factorial(n-1)  # Recursive call for n-1

# Get the input number from the command line arguments
f = factorial(int(sys.argv[1]))

# Output the result of the factorial computation
print(f)


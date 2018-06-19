"""
Program #2: Finding the Greatest Common Divisor (GCD)
COSC 1306, Spring 2016
This program computes and prints the Greatest Common
Divisor between two inputted numbers.
"""

# defining a function that determines the smaller of the two numbers
def smaller_number(i, j):
    if i < j:                   # returns i if i is smaller than j
        return i
    else:                       # returns j if j is smaller than i
        return j

# defining a function that determines the larger of the two numbers
def larger_number(i, j):
    if i > j:                   # returns i if i is larger than j
        return i
    else:                       # returns j if j is larger than i
        return j

# defining a function that calculates the GCD from the given input
def gcd(i, j):
    if larger_number(i, j) % smaller_number(i, j) == 0:     # if the second number is the GCD,
        return abs(j)                                       # then return the second number
    else:
        while i % j != 0:           # continue to loop as long as the remainder doesnt equal 0
            remainder = i % j       # set remainder as a variable to reassign j to remainder
            i = j                   # reassign i to j in order to divide the smaller number by the remainder
            j = remainder           # reassign j to the remainder
        return abs(j)               # returns the GCD


# Takes in two integers from the user
first_num = int(input("Enter First Number: "))
sec_num = int(input("Enter Second Number: "))

# Outputs the GCD
print("GCD is:", gcd(first_num, sec_num))
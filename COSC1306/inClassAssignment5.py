# In class assignment 5, Lists and Strings

# 1. Finding Palindromes

# Function that determines if palindrome
def palindrome(input):
    flag = True
    for i in range(0, len(input)):
        if input[i] != input[-1-i]:
            return False
    return flag

# Takes a string as input
word = input("Enter string: ")

# Prints true if string is a palindrome, otherwise prints false
print("Is a palindrome:", palindrome(word))




# 2. Counting inside a string

# Function that determines frequency of each letter of the keyword in the sentence
def count(sentence, keyword):
    for i in range(0, len(keyword)):
        print(keyword[i], sentence.count(keyword[i]))

# Read two strings, a sentence and a keyword
sen = input("Enter sentence:")
kw = input("Enter keyword:")

# Prints the frequency of each letter of the keyword
count(sen, kw)




# 3. Replacement inside a string

# Function that replaces all occurances of 'good' and 'acceptable' with 'fantastic'
def fantastic(input):
    if input.count('good') > 0:
        while input.count('good') > 0:
            input.insert(input.index('good'), 'fantastic')
            input.remove('good')
    if input.count('acceptable') > 0:
        while input.count('acceptable') > 0:
            input.insert(input.index('acceptable'), 'fantastic')
            input.remove('acceptable')
    input = " ".join(input)
    return input

# Takes string as input
string = input("Enter string:")

# Converts string to list
stringList = string.split()

# Prints the new string
print(fantastic(stringList))


# 4. List manipulation (not complete)

# Import the string module
import string

# Takes a number K as a string input, converts it to a list and assigns the variable numOfInt
k = input("Enter number: ")
klist = list(k)
numOfInt = 0

# Converts strings to integers and counts integers
for i in range(0, len(k)):
    if klist[i] in string.digits:
        klist[i] = int(klist[i])
    if type(klist[i]) == int:
        numOfInt = numOfInt + 1

# Prints list & number of integers
print(klist)
print("Number of integers:", numOfInt)

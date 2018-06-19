"""
In Class Exercise: Sorting, Searching Review
COSC 1306, Spring 2016
This program takes a file containing a person's name and their corresponding GPA and stores them in a dictionary and
sorted lists, and it also calculates the number of students between a minimum and maximum GPA.
"""

# Function that conducts a Merge Sort for a list sorted by name
def mergeName(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

# Function that conducts a Merge Sort for a list sorted by GPA
def mergeGPA(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i][1] < right[j][1]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

# Function that builds a dictionary from a given file
def BuildDictionary(mydict, studentfile):
    lines = studentfile.readlines()
    for line in lines:
        data = line.split()
        mydict[data[0]] = data[1]
    return mydict

# Function that calculates the number of students between a minimum and maximum GPA from the dictionary
def FindStudentsInDictionary(mydict, mingpa, maxgpa):
    total = 0
    for key in mydict.values():
        if float(key) >= mingpa and float(key) <= maxgpa:
            total += 1
    return total

# Function that builds a list from a given file
def BuildLists(mylist, studentfile):
    lines = studentfile.readlines()
    for line in lines:
        data = line.split()
        mylist.append(data)
    return mylist

# Function that sorts a list using Merge Sort based on the names
def SortListByName(mylist):
    if len(mylist) < 2:
        return mylist[:]
    else:
        middle = len(mylist) // 2
        left = SortListByName(mylist[0:middle])
        right = SortListByName(mylist[middle:])
        return mergeName(left, right)

# Function that sorts a list using Merge Sort based on the GPA
def SortListByGPA(mylist):
    if len(mylist) < 2:
        return mylist[:]
    else:
        middle = len(mylist) // 2
        left = SortListByGPA(mylist[0:middle])
        right = SortListByGPA(mylist[middle:])
        return mergeGPA(left, right)

# Iterative function that calculates the number of students between a minimum and maximum GPA from the list
def StudentsInListIterative(mylist, mingpa, maxgpa):
    total = 0
    for i in range(len(mylist)):
        if float(mylist[i][1]) >= mingpa and float(mylist[i][1]) <= maxgpa:
            total += 1
    return total

# Recursive function that calculates the number of students between a minimum and maximum GPA from the list
def StudentsInListRecursive(mylist, mingpa, maxgpa):
    if len(mylist) < 2:
        if float(mylist[0][1]) >= mingpa and float(mylist[0][1]) <= maxgpa:
            return 1
        else:
            return 0
    else:
        if float(mylist[0][1]) >= mingpa and float(mylist[0][1]) <= maxgpa:
            return 1 + StudentsInListRecursive(mylist[1:], mingpa, maxgpa)
        else:
            return StudentsInListRecursive(mylist[1:], mingpa, maxgpa)

# Opens student file for reading
studentfile = open('gpa.txt', 'r')
# Creates empty list
mylist = []
# Creates empty dictionary
mydict = {}

# Builds dictionary from student file
mydict = BuildDictionary(mydict, studentfile)
# Closes student file to start from the top
studentfile.close()
# Reopens student file to start from the top
studentfile = open('gpa.txt', 'r')
# Builds list from student file
mylist = BuildLists(mylist, studentfile)
# Closes student file
studentfile.close()

# Prints dictionary
print(mydict)
# Prints list before sorting
print(mylist)
# Prints list sorted by name
print(SortListByName(mylist))
# Prints list sorted by GPA
print(SortListByGPA(mylist))

# Asks user to input the minimum and maximum GPA to determine the number of students between them
mingpa = float(input("Enter minimum GPA: "))
maxgpa = float(input("Enter maximum GPA: "))

# Prints results based on method used
print("Number of students in range (dictionary): ", FindStudentsInDictionary(mydict, mingpa, maxgpa))
print("Number of students in range (iterative): ", StudentsInListIterative(mylist, mingpa, maxgpa))
print("Number of students in range (recursive): ", StudentsInListRecursive(mylist, mingpa, maxgpa))

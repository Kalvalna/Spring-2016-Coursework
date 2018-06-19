"""
Program #1: Sharing the Bill
COSC 1306, Spring 2016
This program computes how much each person would pay
when the checks are totaled and tip is added.
"""

#User input for their name and their friends' names
name1 = input("Enter your name: ")
name2 = input("Enter name of friend: ")
name3 = input("Enter name of friend: ")
name4 = input("Enter name of friend: ")
name5 = input("Enter name of friend: ")

#User input for the bill amount for him/her and his/her friends
bill1 = float(input("Enter bill for " + name1 + ": "))
bill2 = float(input("Enter bill for " + name2 + ": "))
bill3 = float(input("Enter bill for " + name3 + ": "))
bill4 = float(input("Enter bill for " + name4 + ": "))
bill5 = float(input("Enter bill for " + name5 + ": "))

#Output blank space for readability
print(" ")

#Output names and bill amount (up to 2 decimal places) for each person
print("Name of Friends:", name1 + ",", name2 + ",", name3 + ",", name4 + ",", name5)
print("Individual bills:", str("%.2f" %bill1) + ",", str("%.2f" %bill2) + ",", str("%.2f" %bill3) + ",", str("%.2f" %bill4) + ",", str("%.2f" %bill5))

#User input for the tip percentage
tip = float(input("Enter tip percentage: "))

#Adds the bills together and then adds the amount for tip and averages it
bill_total = bill1 + bill2 + bill3 + bill4 + bill5
total = bill_total + (bill_total * (tip/100))
average = float("%.2f" %(total/5))

#Outputs the total bill with tip and how much each person pays
print("Total bill plus tip: %.2f" %total)
print("Each person must pay $" + str("%.2f" %average))
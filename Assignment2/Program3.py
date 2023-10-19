## Problem Statement : Write a program which accepts a number from user and prints "Hello" if number is less than 10
##                     otherwise print "Demo".

def Display(iNo):
    if(iNo <= 10):
        print("Hello")
    else:
        print("Demo")

iValue = (int(input("Enter the number : ")))

Display(iValue)
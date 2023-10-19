## Problem Statement : Write a program which accepts one number from user and print that number of * on the screen

def Display(iNo):
    for iCnt in range(1, iNo+1):
        print("*")

iValue = (int(input("Enter the number : ")))

Display(iValue)
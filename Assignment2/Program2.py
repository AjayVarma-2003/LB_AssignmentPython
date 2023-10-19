## Problem Statement : Write a program which accepts a number from user and prints that number of times * on screen using while loop

def Display(iNo):
    iCnt =1
    while iCnt<=iNo:
        print("*")
        iCnt+=1

iValue = (int(input("Enter the number : ")))

Display(iValue)
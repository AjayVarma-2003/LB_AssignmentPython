## Problem Statement : Write a program which accepts two numbers from user and display 1st number 2nd number of times

def Display(iNo, iFrequency):
    for iCnt in range(1, iFrequency+1):
        print(f"{iNo}")

iValue1 = (int(input("Enter the number : ")))
iValue2 = (int(input("Enter the frequency : ")))

Display(iValue1, iValue2)
## Problem Statement : Write a program which accepts one number from user and print that number of even numbers on screen

def PrintEven(iNo):
    if(iNo < 0):
        print("Invalid value")
    
    iEvenNumber = 2
    
    for iCnt in range(1, iNo+1):
        print(f"{iEvenNumber}")
        iEvenNumber+=2

iValue = (int(input("Enter the number : ")))

PrintEven(iValue)
## Problem Statement : Write a program which accepts a number from user and prints even factors of that numbers

def DisplayFactor(iNo):
    if(iNo < 0):
        iNo = -iNo
        
    for iCnt in range(1, int(iNo/2)+1):
        if(iCnt % 2 == 0 and iNo % iCnt == 0):
            print(f"{iCnt}")

iValue = (int(input("Enter the number : ")))

bRet = DisplayFactor(iValue)

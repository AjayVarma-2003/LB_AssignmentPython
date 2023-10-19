## Problem Statement : Write a program which accepts a number from user and check whether it is even or odd

def CheckEven(iNo):
    if(iNo % 2 == 0):
        return True
    else:
        return False

iValue = (int(input("Enter the number : ")))

bRet = CheckEven(iValue)

if(bRet == True):
    print(f"{iValue} is even number")
else:
    print(f"{iValue} is odd number")
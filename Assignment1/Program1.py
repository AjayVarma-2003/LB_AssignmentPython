## Problem Statement : Write a program to divide the two numbers

def Divide(iNo1, iNo2):
    if(iNo2 == 0):
        return False
    
    iAns = iNo1 / iNo2
    return iAns

iValue1 = (int(input("Enter the number : ")))
iValue2 = (int(input("Enter the second number : ")))

iRet = Divide(iValue1, iValue2)

print(f"Division of the numbers is {iRet}")
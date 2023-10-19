## Problem Statement : Write a program to check whether given number is divisible by 5 or not

def Check(iNo):
    if(iNo % 5 == 0):
        return True
    else:
        return False

iValue1 = (int(input("Enter the number : ")))

bRet = Check(iValue1)

if(bRet ==  True):
    print(f"{iValue1} is divisible by 5")
else:
    print(f"{iValue1} is not divisible by 5")
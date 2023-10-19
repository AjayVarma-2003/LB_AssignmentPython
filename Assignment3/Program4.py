## Problem Statement : Write a program which accepts one character from user and change its case

def DisplayConvert(CValue):
    if(CValue.islower()):
        print(f"{CValue.upper()}")
    elif(CValue.isupper()):
        print(f"{CValue.lower()}")

cValue = (str(input("Enter the character : ")))

DisplayConvert(cValue)
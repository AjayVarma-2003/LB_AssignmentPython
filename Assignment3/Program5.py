## Problem Statement : Accept a character from user and check whether it is vowel or not

def ChkVowel(CValue):
    if(CValue == 'a' or CValue == 'e' or CValue == 'i' or CValue == 'o' or CValue == 'u'):
        return True
    else:
        return False

sValue = (str(input("Enter the character : ")))

bRet = ChkVowel(sValue)

if(bRet == True):
    print("It is vowel")
else:
    print("It is not a vowel")
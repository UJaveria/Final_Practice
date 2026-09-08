# Write a while loop that keeps asking the user for a password until they type the correct one.

import re 
while True :
    password = input("Enter password : ")
    isdigit = bool(re.findall("[0-9]+",password))
    isupper = bool(re.findall("[A-Z]+",password))
    islower = bool(re.findall("[a-z]+",password))
    isspec  = bool(re.findall("[!@#$%]+",password))
    islength  = len(password) >= 8
    if isdigit == True and isupper == True and islower == True or isspec == True and islength == True:
        print("Correct Password!")
        break
    else :
        print("Try again!")
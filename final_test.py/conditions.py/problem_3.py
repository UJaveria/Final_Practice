# Given a year, determine and print whether it's a leap year.

year = int(input("Enter year : "))

if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
    print(f"Leap year")
else :
    print("Not Leap year")
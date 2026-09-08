# Given an exam score, print the letter grade using if/elif/else.
score = float(input("Enter your score : "))

if score > 0 :
    if score >= 90 :
        print(f"Grade : A")
    elif score >= 70 :
        print(f"Grade : B")
    elif score >= 50 :
        print(f"Grade : C")
    elif score >= 30 :
        print(f"Grade : D")
    else :
        print(f"Grade : F")
else :
    print("Invalid input!")  


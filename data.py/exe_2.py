# Problem 2 — Intelligent Password Validator
# Ask the user for a password and determine whether it is valid.
# A valid password must:
# Have at least 12 characters
# Contain at least 2 uppercase letters
# Contain at least 2 lowercase letters
# Contain at least 2 digits
# Contain at least 2 special characters
# Have no spaces
# Not contain the user's name
# Not contain "password"
# Not contain three identical characters consecutively
# Instead of simply printing Invalid, display every rule that the password violates.

password = input("Enter your password : ")
username = input("Enter user name : ")
upper_count = 0
lower_count = 0
digit_count = 0
special_count = 0

space = False 
for ch in password :
    if ch == " " :
        space = True
pas_str = password.lower()
if "password" not in pas_str and username not in pas_str :
    if space == False :
        if len(password) >= 12 :
            for ch in password :
                if ch >= "A" and ch <= "Z" :
                    upper_count += 1
                elif ch >= "a" and ch <= "z" :
                    lower_count += 1
                elif ch >= "0" and ch <= "9" :
                    digit_count += 1
                else :
                    special_count += 1
            if upper_count >= 2 and lower_count >= 2 and digit_count >= 2 and special_count >= 2:
                print("Valid Password")
            elif upper_count < 2 :
                print("Not contan Uppercase letters in given range.")
            elif lower_count < 2 :
                print("Not contan Lowercase letters in given range.")
            elif digit_count < 2 :
                print("Not contan digit in given range.")
            elif special_count < 2 :
                print("Not contain special letters in given range.")

        else :
            print("Password length is lesser!")
    else :
        print("Password cannot contain spaces!")
else :
    print("Password cannot contain username and 'password'!")



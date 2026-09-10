# Problem 4 — Caesar Cipher 🔐
# Ask the user for:
# message
# shift
# Encrypt the message using a Caesar cipher.
# Requirements:
# Preserve uppercase letters
# Preserve lowercase letters
# Preserve spaces
# Preserve digits
# Preserve punctuation
# Handle shifts larger than 26
# Handle negative shifts
# Example:
# Input:
# Hello World!
# Shift: 3
# Output:
# Khoor Zruog!
# Then make the program capable of decrypting the encrypted message too.

message = input("Enter your message : ")
shift  = int(input("Enter shift : "))

# Encrypt the message using a Caesar cipher 🔐
encriptionList = []
if shift > 0 and shift <= 26 :
    for ch in message :
        if (ch >= "A" and ch <= "Z") or (ch >= "a" and ch <= "z") :
            new_letter = chr(ord(ch) + shift) 
        elif ch == " " :
            new_letter = " "
        else :
            new_letter = ch
        encriptionList.append(new_letter)
encrypting_message = "".join(encriptionList)
print(encrypting_message)

# Decryption of message 
decryptionList = []
if shift > 0 and shift <= 26 :
    for ch in encrypting_message :
        if (ch >= "A" and ch <= "Z") or (ch >= "a" and ch <= "z") :
            letter = chr(ord(ch) - shift) 
        elif ch == " " :
            letter = " "
        else :
            letter = ch
        decryptionList.append(letter)
decryption_message = "".join(decryptionList)
print(decryption_message)
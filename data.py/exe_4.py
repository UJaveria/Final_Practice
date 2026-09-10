# roblem 5 — Anagram Intelligence
# Ask the user for two strings.
# Determine whether they are anagrams.
# Ignore:
# spaces
# punctuation
# capitalization
# Examples:
# "listen"
# "silent"
# → Anagram
# and:
# "The eyes"
# "They see"
# → Anagram
# Your program should work with arbitrary sentences, not just single words.
import re
str1 = input("Enter string 1 :").lower()
str2 = input("Enter string 2 :").lower()

str1 = str1.replace(" ","")
str2 = str2.replace(" ","")
punc_1 = re.findall("[~`!@#$%^&*():;\"'<>,.?/|]+",str1)
punc_2 = re.findall("[~`!@#$%^&*():;\"'<>,.?/|]+",str2)

for p1 in punc_1 : 
    str1 = str1.replace(p1,"")

for p2 in punc_2 : 
    str2 = str2.replace(p2,"")

length_1 = len(str1)
length_2 = len(str2)
if length_1 == length_2 :
    is_anagram = True
    for ch in str1 :
        if ch not in str2 :
            is_anagram = False
    if is_anagram == True :
        print("Anagram")
    else :
        print("Not Anagram")
else :
    print("Strings are not of same length, so they cannt anagram")
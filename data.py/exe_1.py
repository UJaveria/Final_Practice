import re
# Write a program that takes a sentence from the user and produces:

sentence = input("Enter sentence : ")

# Total number of characters
total_characters = 0

for ch in sentence :
    total_characters += 1
print(f"Total characters : {total_characters}")

total_characters = 0
# Total number of characters excluding spaces
new_string = sentence.replace(" ","")
for ch in new_string :
    total_characters += 1
print(f"Total characters without spaces : {total_characters}")

# Number of words
word_list = sentence.split(" ")
words_count = 0
for word in word_list :
    words_count += 1

print(f"Total words in sentence are : {words_count}")

# Number of vowels
num_vowels = 0
for ch in sentence.lower() :
    if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u" :
        num_vowels += 1
print(f"Total vowels : {num_vowels}")

# Number of consonents
num_consonents = 0
for ch in sentence.lower() :
    if ch >= "a" and ch <= "z" :
        if ch != "a" and ch != "e" and ch != "i" and ch != "o" and ch != "u" :
            num_consonents += 1
print(f"Total consonents : {num_consonents}")

# Number of digits
num_digit = 0
for dig in sentence :
    num = re.findall("[0-9]+",dig)
    if num :
        num_digit += 1
print(f"Total digit : {num_digit}")

# Number of special characters
num_special = 0
for ch in sentence :
    special = re.findall("[!,:;'.?@#$%^&~]",ch)
    if special :
        num_special += 1
print(f"Total special characters : {num_special}")

# Number of uppercase letters
num_uppercase = 0
for ch in sentence :
    if ch >= "A" and ch <= "Z" :
        num_uppercase += 1
print(f"Total uppercase : {num_uppercase}")

# Number of lowercase letters
count_lowercase = 0
for ch in sentence :
    if ch >= "a" and ch <= "z" :
        count_lowercase += 1
print(f"Total lowercase : {count_lowercase}")

# The longest word
words = sentence.split()
len_list = []
for w in words :
    length = len(w)
    len_list.append(length)

for w in words :
    if max(len_list) == len(w) :
        print(f"Longest word : {w}")

# The Shortest word 
word_list = sentence.split()
length_list = []
for w in word_list :
    length = len(w)
    length_list.append(length)

for w in word_list :
    if min(length_list) == len(w) :
        print(f"The shortest word : {w}")

#  The most frequently occurring character
ch_list = []
for ch in sentence.lower().replace(" ","") :
    ch_list.append(ch)
ch_list = list(set(ch_list))

numberList = []
chardict = dict()
for c in ch_list :
    countChar = 0
    for character in sentence.lower().replace(" ","") :
        if c == character :
            countChar += 1
    numberList.append(countChar)
    chardict.update({c : countChar})

maximum = max(numberList)
for key,val in chardict.items() :
    if val == maximum :
        print(f"The most frequent character : {key,":",val}")

# Whether the sentence is a palindrome after ignoring spaces, punctuation, and case

text = sentence.lower().replace(" ","")
num = re.findall("[0-9]+",text)
special = re.findall("[!,:;'.?@#$%^&~]",text)
strnum = " ".join(num)
spec_ch = " ".join(special)
text = text.replace(strnum,"")
text = text.replace(spec_ch,"")

reverse_text = text[::-1]
if text == reverse_text :
    print("Palindrome")
else :
    print("Not a Palindrome")

# Problem 6 — Word Frequency Engine
# Given a paragraph, generate a frequency table of every word.
# Ignore:
# capitalization
# punctuation
# Example:
# Python is easy. Python is powerful. Python is popular.
# Expected concept:
# python → 3
# is     → 3
# easy   → 1
# powerful → 1
# popular → 1
# Then display the most frequent word.

import re
# Taking lines from user
para_list = []
while True :
    line = input("Enter line : ").lower()
    if line == "" :
        break
    para_list.append(line)
# Converting lines into Paragraph 
paragraph = " ".join(para_list)
# Eliminating punctuations
punc = re.findall("[~`!@#$%^&*():;\"'.,?/|]",paragraph)

for p in punc :
    paragraph = paragraph.replace(p,"")
# Converting into form of list
paragraph = paragraph.split()
# Taking words and their count in dictionary
words = dict() 
for word in paragraph :
    count = 0
    for l in paragraph :
        if word == l :
            count += 1
    words.update({word : count})
# Printing word and its value one-by-one
for word,val in words.items() :
    print(word,":",val)
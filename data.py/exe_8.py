
# Problem 10 — Advanced Text Cleaner
# Create a text-cleaning program.
# Input may contain:
# "   HELLO!!!   My   name is   Jia...   I LOVE Python!!!   "
# Your program must:
# Remove leading/trailing whitespace
# Convert text to a consistent case
# Remove unnecessary punctuation
# Replace multiple spaces with a single space
# Correctly preserve words
# Produce a clean sentence
# Expected style:
# hello my name is jia i love python
# text = input("Enter your text : ")
import re 
text = "   HELLO!!!   My   name is   Jia...   I LOVE Python!!!   "
# eliminating leading and trailing whitespaces
text = text.strip()
# converting to lower case
text = text.lower()
# replacing multiple spaces with single space
spaces = re.findall("[' ']+",text)
for sp in spaces :
    text = text.replace(sp," ")

# removing punctuations
punctuation  = re.findall("[`~!@#$%^&*()':;?/.,\"]",text)
for punc in punctuation :
    text = text.replace(punc,"")
    
print(text)
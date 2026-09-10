# Problem 7 — Remove Duplicate Characters
# Write a program that removes repeated characters while preserving the first occurrence order.
# Example:
# Input:
# programming
# Output:
# progamin
# Another:
# Input:
# mississippi
# Output:
# misp
# Case sensitivity matters

text = input("Enter text : ")
# collecting characters and their counts in dictionary
my_dic = dict()
for ch in text :
    count = 0
    for i in text :
        if ch == i :
            count += 1
    my_dic.update({ch : count})
print(my_dic)
# Appending characters available in dictionary into a list
my_list = []
for key in my_dic :
    my_list.append(key)
# Again making word from characters in list
new_word = "".join(my_list)
print(new_word)
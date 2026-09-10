# Problem 8 — Run-Length Decoder
# Now reverse Problem 3.
# Input:
# a3b2c4d1a2
# Output:
# aaabbccccdaa
# Your program should correctly decode any valid compressed string.

compressed_str = input("Enter your compressed string : ")
length = len(compressed_str)
my_list = []
i = 0
j = 1
try :
    while length > 0 :
        ch = compressed_str[i]
        num = compressed_str[j]
        my_list.append(ch * int(num))
        length -= 2
        i += 2
        j += 2
    words = "".join(my_list)
    print(words)
except Exception as e :
    print(e)
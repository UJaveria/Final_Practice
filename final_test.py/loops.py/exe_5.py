# Write a nested loop that prints a right-aligned triangle pattern of stars, with the number of rows set
# by a variable.

rows = 5
col = 1

for i in range(1,rows+1) :
    print((rows-i) * " ",end="")
    print(i * "*")
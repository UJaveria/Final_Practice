# Loop through a list of names and print each with its position number starting from 1 (not 0).
names = ["Maha","Zara","Laiba","Sana"]


for index in enumerate(names,start=1) :
    print(index)
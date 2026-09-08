# Given two equal-length lists (names, scores), zip them into a list of tuples, then sort that list by
# score descending.

from operator import itemgetter
names = ["javeria","maha","priya"]
scores= [90,87,92]
tup = list(zip(names,scores))

result = sorted(tup, key=itemgetter(1) , reverse= True)
print(result)

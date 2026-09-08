# Write a function that reads a CSV, filters rows by a condition, and writes the filtered rows to a new CSV 
# file.

import csv

mydata = []
with open("data.csv","r") as f :
    reader = csv.reader(f)
    header = next(reader)
    for dic in reader :
        if int(dic[1]) <= 18 :
           mydata.append(dic)
        else :
            continue

with open("filteredfile.csv","w",newline="") as f :
    writer = csv.writer(f)
    writer.writerow(["name","age","city"])
    for i in mydata :
        writer.writerow(i)
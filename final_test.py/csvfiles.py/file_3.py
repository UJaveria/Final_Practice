# Read a CSV using DictReader and print only the rows where a given column matches a given value.

import csv 

search_name = input("Enter name : ")

with open("student.csv","r") as f :
    reader = csv.DictReader(f)
    for dic in reader :
        if dic["name"].lower() == search_name.lower() :
            print(dic)
        
# Read a CSV file and print the total number of rows (excluding the header).
import csv

total_rows = 0

with open("student.csv","r") as file :
    reader = csv.reader(file)
    header = next(reader)
    # print(f"Header : {header}")
    for row in reader :
        total_rows += 1

print(f"Total rows : {total_rows}")

# Create a CSV file with a header row and 3 rows of sample data using the csv module.

import csv

with open("student.csv","w",newline="") as file :
    writer = csv.writer(file)
    writer.writerow(["name","age","city"])
    writer.writerows([
        ['Ali', '21', 'Lahore'],
        ['Sara', '22', 'Karachi'],
        ['Bilal', '20', 'Faisalabad']
    ])
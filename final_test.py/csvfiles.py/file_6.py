# Given a CSV of transactions with a date column, compute total sales grouped by month (parsing dates 
# manually, no pandas) and write the result as a new summary CSV with columns month total.

import csv
dates = []
with open("transaction.csv","r") as f :
    reader = csv.DictReader(f)
    header = next(reader)
    for dic in reader :
        d = dic["date"].split("-")
        dates.append(d[1])

my_set = set(dates)
my_list = list(my_set)

sort_list = sorted(my_list)
print(sort_list)

total_list = []
for i in sort_list :
    with open("transaction.csv","r") as f :
        reader = csv.DictReader(f)
        total = 0
        for dic in reader :
            d = dic["date"].split("-")
            if d[1] == i :
                total += int(dic["amount"])
        total_list.append(total)

final_data =  zip(sort_list,total_list)

with open("summary.csv","w",newline="") as f :
    writer = csv.writer(f)
    writer.writerow(["date","totals"]) 
    for month, total in final_data :
        writer.writerow([month,total])
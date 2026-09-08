# Given a dict mapping departments to lists of (employee,	salary)	tuples,	compute	the	average
# salary per department AND the department with the overall highest average —	no external , no external libraries

my_dict = {
    "IT": [("Ali", 50000), ("Sara", 70000)],
    "HR": [("Ahmed", 40000), ("Ayesha", 60000)]
}

heighest_sal = float("-inf")
heighest_sal_dep = None
for key,val in my_dict.items() :
    total = 0
    for tup in val :
        total += tup[1]
    avg_sal = total / len(val)
    if avg_sal > heighest_sal :
        heighest_sal = avg_sal
        heighest_sal_dep = key
    print(f"Department : {key}\nAverage Salary : {avg_sal}")

print(f"Heighest average salrary is : {heighest_sal}\nDepartment with heighest average salary : {heighest_sal_dep}")
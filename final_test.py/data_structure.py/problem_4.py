# Given a list of employee dicts (name, department), group them into a new dictionary mapping
# department → list of employee names.

num = int(input("How many employee you wants to add : "))

info = []


for i in range(1,num+1) :
    employee = dict()

    name = input("Enter employee name : ")
    department = input("Enter department name : ")
    employee["name"] = name
    employee["department"] = department
    info.append(employee)

dep_set = set()
my_list = []
for dic in info :
    dep_set.add(dic["department"])
my_list = list(dep_set)

new_dict = dict()
for i in my_list :
    name_list = []
    for dic in info :
        if dic["department"] == i :
            name_list.append(dic["name"])
    new_dict.update({i : name_list})

print(new_dict)
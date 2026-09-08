# Given a JSON file with departments → employees → skills (3 levels deep), build a flat list of every
# unique skill company-wide with a count of how many employees have each one.
import json

skills = []
with open("jsonfile.json",'r') as f :
    dic = json.load(f)
    for key, val in dic.items() :
        for k , v in val.items() :
            for i in v :
                skills.append(i)

skill_set = set(skills)
skill_list = list(skill_set)


final_list = []
for i in skill_list :
    with open("jsonfile.json","r") as f :
        dic = json.load(f)
        count = 0
        my_skilldic = dict()
        for key,val in dic.items() :
            for k , v in val.items() :
                if i in v :
                    count += 1
        my_skilldic.update({"skill" : i , "count" : count})
    final_list.append(my_skilldic)
print(final_list)
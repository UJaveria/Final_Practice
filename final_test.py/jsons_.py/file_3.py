# Save a dictionary to a .json file, then load it back and confirm the loaded data matches the original.

import json

info = {
    "name" : "Maha",
    "age"  : 19,
    "skills" : ["programming","drawing"],
    "languages" : ["Python","C++","Javascript"] 
}

with open("new.json","w") as file :
    json.dump(info, file, indent=4)

with open("new.json","r") as f :
    data = json.load(f)
    if info == data :
        print("Matched")
    else :
        print("Not Matched")
# Write a function that appends a new record to an existing JSON file (a list of dicts) without overwriting
# the previous entries.

import json


def append_new_record(record) :

    try :
        with open("orders.json","r") as file :
            data = json.load(file)

        data.append(record)

        with open("orders.json","w") as file :
            json.dump(data,file,indent=4)
            
    except Exception as e :
        print(e)


record = {
        "id": 6,
        "item": "Phone",
        "amount": 120000
    }

append_new_record(record)
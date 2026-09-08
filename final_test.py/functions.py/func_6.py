# Write flatten(nested_list) that takes an arbitrarily nested list (lists within lists within lists) and returns
# one flat list, using recursion.

def flatten(nested_list, new_list = []) :
    for i in nested_list :
        if isinstance(i,list) == True :
            flatten(i,new_list)
        else :
            new_list.append(i)
    return new_list

nested_list = [1,[2,[3,4,5]]]
print(flatten(nested_list))
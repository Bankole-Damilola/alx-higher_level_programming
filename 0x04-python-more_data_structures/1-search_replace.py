#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list == []:
        return my_list
    new_list = []
    for elem in my_list:
        if elem != search:
            new_list.append(elem)
        else:
            new_list.append(replace)
    return new_list

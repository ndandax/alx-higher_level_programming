#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for i in range(len(my_list)):
        if my_list[i] == search:
            my_list.append(replace)
        else:
            my_list.append(my_list[i])
    return (my_list)

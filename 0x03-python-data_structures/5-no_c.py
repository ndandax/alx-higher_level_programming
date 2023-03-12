#!/usr/bin/python3
def no_c(my_string):
    copy = list(my_string)
    for i in my_string:
        if i != 'C' and i != 'c':
            return ("".join(copy))

#!/usr/bin/python3
def no_c(my_string):
    copy = list(my_string)
    for copy in my_string:
        if copy != 'C' and copy != 'c':
            return ("".join(copy))

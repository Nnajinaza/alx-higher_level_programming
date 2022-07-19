#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end='')
        except (ValueError, TypeError, NameError):
            i += 1
        else:
            count += 1
            i += 1
    print()
    return count

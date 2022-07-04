#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    else:
        for value in range(len(my_list)):
            biggest = my_list[0]
            if value > biggest:
                biggest = my_list[value - 1]
                return biggest

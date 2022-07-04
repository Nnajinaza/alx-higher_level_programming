#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    for nos in range(len(my_list)):
        mul = nos % 2
        if mul == 0:
            lis = True
            return lis
        else:
            lis = False
            return lis

#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    lis = [True if nos % 2 == 0 else False for nos in my_list]
    return lis

#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0

    if my_list and len(my_list):
        score = 0
        weight = 0
        for i in my_list:
            score += (i[0] * i[1])
            weight += i[1]
        return score/weight

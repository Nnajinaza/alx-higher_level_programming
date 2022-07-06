#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_matrix = my_list.copy()
    for i in range(len(my_matrix)):
        if my_matrix[i] == search:
            my_matrix[i] = replace
    return my_matrix

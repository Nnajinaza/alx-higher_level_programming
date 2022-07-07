#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    score = max(a_dictionary, key=lambda i: a_dictionary[i])
    return score

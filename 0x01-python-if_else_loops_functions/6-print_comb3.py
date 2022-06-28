#!/usr/bin/python3
for i in range(0, 9):
    for n in range(1, 10):
        if i != n and i < n and i != 8:
            print("{}{}".format(i, n), end=', ')
        elif i != n and i < n and i == 8:
            print("{}{}".format(i, n))

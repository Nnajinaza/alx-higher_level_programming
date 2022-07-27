#!/usr/bin/python3

l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)

def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)

def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)

a = (1, 2)
b = (1, 2)
a is b

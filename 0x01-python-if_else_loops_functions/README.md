**0x01-python-if_else_loops_functions**

This directory is based of on solution which implements the if, elif, else, and loop statements to solve the various problem given on each task.

**TASK 0: Positive anything is better than negative nothing**

This program will assign a random signed number to the variable number each time it is executed. 

```
chinaza@ubuntu:~/0x01$ ./0-positive_or_negative.py 
-6 is negative
chinaza@ubuntu:~/0x01$ ./0-positive_or_negative.py 
0 is zero
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
8 is positive
chinaza@ubuntu:~/0x01$ 
```

**TASK 1: The last digit**
This program will assign a random signed number to the variable number each time it is executed, in order to print the last digit of the number stored in the variable number.

```
chinaza@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 8235 is 5 and is less than 6 and not 0
chinaza@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -846 is -6 and is less than 6 and not 0
chinaza@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 63474 is 4 and is less than 6 and not 0
chinaza@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -6700 is 0 and is 0
chinaza@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 5247 is 7 and is greater than 5
chinaza@ubuntu:~/0x01$ ./1-last_digit.py
```

**TASK 2: I sometimes suffer from insomnia.**
Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.
```
chinaza@ubuntu:~/0x01$ ./2-print_alphabet.py
abcdefghijklmnopqrstuvwxyzchinaza@ubuntu:~/0x01$
```

**TASK 3: When I was having that alphabet soup, I never thought that it would pay off**
Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line. Print all the letters except q and e.

```
chinaza@ubuntu:~/0x01$ ./3-print_alphabt.py
abcdfghijklmnoprstuvwxyzchinaza@ubuntu:~/0x01$
```

**TASK 4: Hexadecimal printing**
Write a program that prints all numbers from 0 to 98 in decimal and in hexadecimal

```
chinaza@ubuntu:~/0x01$ ./4-print_hexa.py
0 = 0x0
1 = 0x1
2 = 0x2
3 = 0x3
4 = 0x4
5 = 0x5
6 = 0x6
7 = 0x7
8 = 0x8
9 = 0x9
10 = 0xa
11 = 0xb
12 = 0xc
13 = 0xd
14 = 0xe
15 = 0xf
16 = 0x10
17 = 0x11
18 = 0x12
...
96 = 0x60
97 = 0x61
98 = 0x62
chinaza@ubuntu:~/0x01$
```

**TASK 5: 00...99**
Write a program that prints numbers from 0 to 99.

```
chinaza@ubuntu:~/0x01$ ./5-print_comb2.py
00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99
chinaza@ubuntu:~/0x01$ 
```

**TASK 6:  Inventing is a combination of brains and materials.**

Write a program that prints all possible different combinations of two digits.
```
chinaza@ubuntu:~/0x01$ ./6-print_comb3.py
01, 02, 03, 04, 05, 06, 07, 08, 09, 12, 13, 14, 15, 16, 17, 18, 19, 23, 24, 25, 26, 27, 28, 29, 34, 35, 36, 37, 38, 39, 45, 46, 47, 48, 49, 56, 57, 58, 59, 67, 68, 69, 78, 79, 89
chinaza@ubuntu:~/0x01$ 
```

**TASK 7: Islower**
Write a function that checks for lowercase character.

```
chinaza@ubuntu:~/0x01$ cat 7-main.py
#!/usr/bin/env python3
islower = __import__('7-islower').islower

print("a is {}".format("lower" if islower("a") else "upper"))
print("H is {}".format("lower" if islower("H") else "upper"))
print("A is {}".format("lower" if islower("A") else "upper"))
print("3 is {}".format("lower" if islower("3") else "upper"))
print("g is {}".format("lower" if islower("g") else "upper"))

chinaza@ubuntu:~/0x01$ ./7-main.py
a is lower
H is upper
A is upper
3 is upper
g is lower
chinaza@ubuntu:~/0x01$
```

#This directory has files of different task which contains scripts and programs to do different things

##TASK 0: Run Python file

Write a shell script that runs a Python script, the file name will be stored in an environmental variable $PYFILE

<pre>
chinaza@ubuntu:~/py/0x00$ cat main.py
#!/usr/bin/python3
print("Best School")

chinaza@ubuntu:~/py/0x00$ export PYFILE=main.py
chinaza@ubuntu:~/py/0x00$ ./0-run
Best School
chinaza@ubuntu:~/py/0x00$
<pre>

##TASK 1: Run inline
Write a shell script tht run Python code, and it will be saved in the environment variable $PYCODE

<pre>
chinaza@ubuntu:~/py/0x00$ export PYCODE='print(f"Best School: {88+10}")'
chinaza@ubuntu:~/py/0x00$ ./1-run_inline 
Best School: 98
chinaza@ubuntu:~/py/0x00$ 
<pre>

##TASK 2: Hello, print
Write a Python script that prints a statement has a special character followed by a new line using the function "print"

<pre>
chinaza@ubuntu:~/py/0x00$ ./2-print.py 
"Programming is like building a multilingual puzzle
chinaza@ubuntu:~/py/0x00$
<pre>

##TASK 3: Print integer
This program prints an integer stored in a variable follwed by a string the a new line

<pre>
chinaza@ubuntu:~/py/0x00$ ./3-print_number.py
98 Battery street
chinaza@ubuntu:~/py/0x00$
<pre>

##TASK 4: Print float
This code prints out the float stored in the variable number with a precision of 2 digits

<pre>
chinaza@ubuntu:~/py/0x00$ ./4-print_float.py
Float: 3.14
chinaza@ubuntu:~/py/0x00$ 
<pre>

##TASK 5: Print string
This code print 3 times a string stored in the variable str, followed by its first 9 characters.print 3 times a string stored in the variable str, followed by its first 9 characters.

<pre>
chinaza@ubuntu:~/py/0x00$ ./5-print_string.py 
Holberton SchoolHolberton SchoolHolberton School
Holberton
chinaza@ubuntu:~/py/0x00$ 
<pre>

##TASK 6:Play with strings
This code concats two strings together

<pre>
chinaza@ubuntu:~/py/0x00$ ./6-concat.py
Welcome to Holberton School!
chinaza@ubuntu:~/py/0x00$ wc -l 6-concat.py
5 6-concat.py
chinaza@ubuntu:~/py/0x00$ 
<pre>

##TASK 7: Copy-Cut-Paste
This code prints out parts of a string

<pre>
chinaza@ubuntu:~/py/0x00$ ./7-edges.py
First 3 letters: Hol
Last 2 letters: on
Middle word: olberto
chinaza@ubuntu:~/py/0x00$ 
<pre>

##TASK 8: Create a new sentence
This code separates sentences into differents new strings and concats them together to create a new sentence

<pre>
chinaza@ubuntu:~/py/0x00$ ./8-concat_edges.py
object-oriented programming with Python
chinaza@ubuntu:~/py/0x00$ 
<pre>

##TASK 9: Easter Egg
Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.

<pre>
chinaza@ubuntu:~/py/0x00$ ./9-easter_egg.py
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
chinaza@ubuntu:~/py/0x00$
<pre>

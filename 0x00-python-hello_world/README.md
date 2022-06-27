This directory has files of different task which contains scripts and programs to do different things

TASK 0: Run Python file

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

TASK 1: Run inline
Write a shell script tht run Python code, and it will be saved in the environment variable $PYCODE

<pre>
chinaza@ubuntu:~/py/0x00$ export PYCODE='print(f"Best School: {88+10}")'
chinaza@ubuntu:~/py/0x00$ ./1-run_inline 
Best School: 98
chinaza@ubuntu:~/py/0x00$ 
<pre>

TASK 2: Hello, print
Write a Python script that prints a statement has a special character followed by a new line using the function "print"

<pre>
chinaza@ubuntu:~/py/0x00$ ./2-print.py 
"Programming is like building a multilingual puzzle
chinaza@ubuntu:~/py/0x00$
<pre>

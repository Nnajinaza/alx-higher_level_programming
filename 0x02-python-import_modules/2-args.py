#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = len(sys.argv) - 1
    if i == 0:
        print("0 arguments.")
    elif i == 1:
        print("{} argument:".format(i))
    else:
        print("{} arguments:".format(i))
    for n in range(i):
        print("{}: {}".format(n + 1, str(sys.argv[n + 1])))

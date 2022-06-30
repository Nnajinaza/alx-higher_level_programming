#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    if ((len(sys.argv) - 1) != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    option = {"+": add, "-": sub, "*": mul, "/": div}

    if sys.argv[2] not in option:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{} {} {} = {}".format(a, sys.argv[2], b, option[sys.argv[2]](a, b)))

#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    nargs = len(sys.argv) - 1
    if nargs != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    op = sys.argv[2]
    if op != '+' and op != '-' and op != '*' and op != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    from calculator_1 import add, sub, mul, div
    x = int(sys.argv[1])
    y = int(sys.argv[3])

    if op == '+':
        print("{} + {} = {}".format(x, y, add(x, y)))
    elif op == '-':
        print("{} - {} = {}".format(x, y, sub(x, y)))
    elif op == '*':
        print("{} * {} = {}".format(x, y, mul(x, y)))
    else:
        print("{} / {} = {}".format(x, y, div(x, y)))

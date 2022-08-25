#!/usr/bin/python3
from sys import argv
from calculator_1 import addition, subtraction, multiplication, division
if __name__ != "__main__":
    exit()

argc = len(argv) - 1
if argc != 3:
    print("Usage: {:s} <a> <operator> <b>".format(argv[0]))
    exit(1)
elif argv[2] == '+':
    func = addition
elif argv[2] == '-':
    func = subtraction
elif argv[2] == '*':
    func = multiplication
elif argv[2] == '/':
    func = division
else:
    print("Unknown operator. Available operators: +, -, *, and /")
    exit(1)

result = func(int(argv[1]), int(argv[3]))
print("{:d} {:s} {:d} = {:d}".format(int(argv[1]),
    argv[2], int(argv[3]), result))

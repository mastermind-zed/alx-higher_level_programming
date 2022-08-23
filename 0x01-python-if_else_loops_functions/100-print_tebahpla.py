#!/usr/bin/python3
for digit in reversed(range(97, 123)):
    print("{:c}".format(digit if (digit % 2 == 0) else (digit - 32)), end='')

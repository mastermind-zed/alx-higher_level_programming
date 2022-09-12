#!/usr/bin/python3

def magic_calculation(a, b):
    """ Python function def magic_calculation(a, b): that does exactly the same as the following """

    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            result += a ** b / i
        except Exception:
            result = b + a
            break
    return result

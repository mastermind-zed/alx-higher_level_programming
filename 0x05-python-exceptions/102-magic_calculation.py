#!/usr/bin/python3

def magic_calculation(a, b):
    """ Python function def magic_calculation(a, b): that does exactly the same as the following """

    ans = 0
    for y in range(1, 3):
        try:
            if y > a:
                raise Exception('Too far')
            ans += a ** b / y
        except Exception:
            ans = b + a
            break
    return (ans)

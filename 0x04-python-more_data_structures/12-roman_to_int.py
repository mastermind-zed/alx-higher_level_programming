#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    numeral = {'I': 1, 'V': 5, 'X': 10, 'IV': -1, 'IX': -1, 'L': 50, 'C': 100,
               'D': 500, 'M': 1000, 'CM': -100, 'XC': -10}
    num = []
    roman_string += 'z'
    for first, second in zip(roman_string, roman_string[1:]):
        try:
            num.append(numeral[first + second])
        except:
            num.append(numeral.get(first))
    return sum(num)

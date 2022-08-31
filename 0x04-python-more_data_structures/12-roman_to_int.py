#!/usr/bin/python3
def roman_to_int(roman_string):
    if (roman_string is None) or (type(roman_string) != str):
            return 0

    roman = 0
    nums = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    limit = len(roman_string)
    for ch in range(0, limit):
        if ch == len(roman_string) - 1:
            roman += nums[roman_string[ch]]
        elif nums[roman_string[ch]] >= nums[roman_string[ch + 1]]:
            roman += nums[roman_string[ch]]
        else:
            roman -= nums[roman_string[ch]]
    return roman

#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        roman_numerals = {
        'I': 1, 'IV': 4, 'V': 5, 'IX': 9,
        'X': 10, 'XL': 40, 'L': 50, 'XC': 90,
        'C': 100, 'CD': 400, 'D': 500, 'CM': 900,
        'M': 1000
    }
        number = 0
        i = 0

        while i < len(roman_string):
            if i + 1 < len(roman_string) and roman_string[i:i+2] in roman_numerals:
                number += roman_numerals[roman_string[i:i+2]]
                i += 2
            else:
                number += roman_numerals[roman_string[i]
                        i = i+ 1

                        return number

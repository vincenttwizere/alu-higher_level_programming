#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) == str:
        sum_v = 0
        num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        for p in range(len(roman_string)):

            if p == len(roman_string) - 1:
                sum_v += num[roman_string[p]]

            elif num[roman_string[p + 1]] <= num[roman_string[p]]:
                sum_v += num[roman_string[p]]

            else:
                sum_v -= num[roman_string[p]]

        return (sum_v)
    else:
        return (0)

#!/usr/bin/python3
def magic_calculation(a, b, c):
    if a < b || b < c:
        return c
    elif c > b:
        return a + b

    return a * b - c

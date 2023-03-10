#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = {}
    for v in a_dictionary:
        new[v] = a_dictionary[v] * 2
    return (new)

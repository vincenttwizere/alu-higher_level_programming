#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    n = 0  # Counter variable
    for n in range(x):
        try:
            print("{}".format(my_list[n]), end="")
            n += 1

        except IndexError:
            break
    print()
    return (n)  # Return number of elem printed
~                                               

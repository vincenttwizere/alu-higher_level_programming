#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    d = 0  # Counter variable
    for d in range(x):
        try:
            print("{}".format(my_list[d]), end="")
            d += 1

        except IndexError:
            break
    print()
    return (d)  # Return number of elem printed
~                                               

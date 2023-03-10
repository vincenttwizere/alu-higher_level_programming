#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    t = 0  # Counter variable
    for t in range(x):
        try:
            print("{}".format(my_list[t]), end="")
            t += 1

        except IndexError:
            break
    print()
    return (t)  # Return number of elem printed


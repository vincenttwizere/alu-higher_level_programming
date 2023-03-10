def safe_print_list(my_list=[], x=0):
    try:
        for q in range(x):
            print(my_list[q], end=' ')
    except IndexError:
        pass
    finally:
        print('\n', end='')
    return min(x, len(my_list))

~                                               

#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    n = len(my_list) - 1
    for i in range(0, n // 2):
        temp = my_list[i]
        my_list[i] = my_list[n - i]
        my_list[n - i] = temp
    for k in my_list:
        print("{:d}".format(k))

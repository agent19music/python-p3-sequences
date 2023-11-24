#!/usr/bin/env python3

def print_fibonacci(length):
    my_list =[]
    if length == 0:
        return my_list
    if length > 0 :
        my_list.append(0)
    if length > 1 :
        my_list.append(1)
    while len(my_list) < length:
        my_list.append(my_list[-1] + my_list[-2])
    return my_list

pass
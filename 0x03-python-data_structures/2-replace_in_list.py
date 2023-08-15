#!/usr/bin/python3

def replace_in_list(my_list, it, element):
    if it < 0 or it >= len(my_list):
        return my_list
    my_list[it] = element
    return my_list

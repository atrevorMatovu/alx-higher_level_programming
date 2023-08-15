#!/usr/bin/python3

def element_at(my_list, it):
    if it >= len(my_list) or it < 0:
        return None
    return my_list[it]

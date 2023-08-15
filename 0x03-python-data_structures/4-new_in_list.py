#!/usr/bin/python3


def new_in_list(my_list, index, new_element):
    newlist = my_list[:]
    if index < 0 or index > len(my_list) - 1:
        return new_list

    newlist[index] = new_element
    return newlist

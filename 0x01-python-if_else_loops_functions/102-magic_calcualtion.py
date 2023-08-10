#!/usr/bin/python3

def magic_calculation(l, m, n):
    if (l < m):
        return n
    elif (n > m):
        return l + m
    else:
        return (l * m) - n

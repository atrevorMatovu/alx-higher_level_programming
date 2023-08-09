#!/usr/bin/python3
def uppercase(str):
    for d in str:
        d = ord(d)
        if d >= 97 and d <= 122:
            d -= 32
        print("{}".format(chr(d)), end='')
    print("{}".format(""))

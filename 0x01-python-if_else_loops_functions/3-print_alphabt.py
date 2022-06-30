#!/usr/bin/python3
for letter in range(ord('a'), ord('z')+1):
    if chr(letter) != (ord('q')) and chr(letter) != (ord('e')):
        print("{}".format(chr(letter)), end="")

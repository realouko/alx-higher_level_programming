#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    keylist = list(a_dictionary.keys())
    keylist.sort()
    for i in keylist:
        print("{}: {}".format(i, a_dictionary.get(i)))

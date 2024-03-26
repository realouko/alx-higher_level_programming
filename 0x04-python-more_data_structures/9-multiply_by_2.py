#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    newdict = a_dictionary.copy()
    allkeys = list(newdict.keys())

    for i in allkeys:
        newdict[i] *= 2

    return (newdict)

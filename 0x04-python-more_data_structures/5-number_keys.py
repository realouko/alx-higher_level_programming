#!/usr/bin/python3

def number_keys(a_dictionary):
    count = 0
    allkeys = list(a_dictionary.keys())

    for i in allkeys:
        count += 1

    return (count)

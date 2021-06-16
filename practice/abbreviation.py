#!/bin/python3

import math
import os
import random
import re
import sys
import string

#
# Complete the 'abbreviation' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def abbreviation(a, b):
    # Write your code here
    # print(string.ascii_lowercase)
    upperCountA = sum(1 for c in a if c.isupper())

    if step(a, b, 0, upperCountA, len(b)):
        return "YES"
    return "NO"

def step(a, b, i, upperCountA, l):
    
    if a == b or a.upper() == b:
        return True

    if a.isupper() and len(a) > l:
        return False

    if len(a) <= l:
        return False

    if i >= len(a):
        return False

    if a[i].isupper():
        return step(a, b, i+1, upperCountA, l)

    if upperCountA > l:
        return False


    # print(" " + str(a) + " " + str(i))
    return step(a.replace(a[i], "", 1), b, i, upperCountA, l) or step(a.replace(a[i], a[i].upper()), b, i+1, upperCountA+a.count(a[i]), l)     


print(abbreviation("abcde", "ABDE")) # YES
print(abbreviation("beFgH", "EFH")) # YES
print(abbreviation("aAbAb", "ABAB")) # YES
print(abbreviation("abAAb", "AAA")) # YES
print(abbreviation("Pi", "P")) # YES
print(abbreviation("abAxxaBa", "ABA")) # YES
print("------------------------")
print(abbreviation("beFgH", "EFG")) # NO
print(abbreviation("ababbaAbAB", "AABABB")) # NO
print(abbreviation("baaBa", "BAAA")) # NO
print(abbreviation("babaABbbAb", "ABAA")) # NO
print(abbreviation("AaABCD", "ABCD")) # NO
print(abbreviation("KxZQ", "K")) # NO


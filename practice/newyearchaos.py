#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#
# check if number received bribe not sure if will be time efficient
def minimumBribes(q):
    # Write your code here
    s = 0
    l = len(q)
    o = 0
    for i in range(l):
        shift = q[i] - i-1 
        if shift > 2:
            return "Too chaotic"
        s+=abs(shift)
    return s

print(minimumBribes([2, 1, 5, 3, 4]))

print(minimumBribes([2, 5, 1, 3, 4]))

print(minimumBribes([1, 2, 5, 3, 7, 8, 6, 4]))
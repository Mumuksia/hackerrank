#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def makeAnagram(a, b):
    # Write your code here
    b = sorted(b)
    a = sorted(a)

    count = 0
    i=0
    j=0
    while (len(a)-i > 0) and (len(b)-j) > 0:
        if (a[i] == b[j]):
            count+=1
            i+=1
            j+=1
        elif a[i] > b[j]:
            j +=1
        else:
            i+=1
    print(count)
    return len(a) + len(b) - 2*count

print(makeAnagram("cde","dcf"))
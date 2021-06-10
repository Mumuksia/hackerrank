import math
import os
import random
import re
import sys

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

def luckBalance(k, contests):
    # Write your code here
    # sort by value take first k important
    sum = 0
    t = []
    for i in range(len(contests)):
        if contests[i][1] == 0:
            sum +=contests[i][0]
        else:
            t.append(contests[i][0])

    t = sorted(t, reverse=True)
    print(t)
    if k < len(t):
        for i in range(k):
            sum+=t[i]

        for i in range(k, len(t)):
            sum-=t[i]
    else:
        for i in range(len(t)):
            sum+=t[i]
    return sum

print(luckBalance(3, [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]))
print(luckBalance(0, [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]))
print(luckBalance(6, [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]))
print(luckBalance(100, [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]))

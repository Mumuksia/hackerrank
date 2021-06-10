import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    arr = sorted(arr)
    if (len(arr) < 2):
        return 0
    min = abs(arr[1] - arr[0])
    for i in range(1, len(arr)):
        if abs(arr[i] - arr[i-1]) < min:
            min = abs(arr[i] - arr[i-1])
    return min

print(minimumAbsoluteDifference([3, -7, 0]))
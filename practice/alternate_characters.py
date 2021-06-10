import math
import os
import random
import re
import sys

#
# Complete the 'alternatingCharacters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternatingCharacters(s):
    # Write your code here
    temp = s[0]
    count = 0
    for i in range(1,len(s)):
        if (s[i] == temp):
            count +=1
        else:
            temp = s[i]
    return count

print(alternatingCharacters("AAA"))
print(alternatingCharacters("ABABA"))
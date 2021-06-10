import math
import os
import random
import re
import sys
import collections

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    if len(s) <= 3:
        return "YES"

    freq = sorted(collections.Counter(s).values())

    if (freq[1] == freq[len(freq) - 1]) and freq[0] == 1:
        return "YES" 
    
    if ((freq[len(freq) - 1] - freq[0]) > 1):
        return "NO"

    if freq[len(freq) - 1] == freq[0]:
        return "YES"

    # print(freq)
    if freq.count(freq[0]) > 1 and freq.count(freq[len(freq) -1]) > 1:
        return "NO"

    #remove!

    if (freq.count(freq[0]) < freq.count(freq[len(freq) -1])) and freq[0] != 1:
        return "NO"


    return "YES"




print(isValid("abcdefghhgfedecba")) # YES
print(isValid("aabbccddeefghi")) # NO
print(isValid("abcc")) #YES
print(isValid("abccc")) #NO
print(isValid("aabbc")) # YES
print(isValid("aaabbbcc")) # NO
print(isValid("aaabbbcccc")) # YES
print(isValid("aaabbbcccr")) #YES
print(isValid("aaabbbbbbbcccr")) #NO
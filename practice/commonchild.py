#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'commonChild' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def commonChild(s1, s2):
    x = len(s1)
    y = len(s2)

    n = [[0 for _ in range(y+1)] for _ in range(x+1)]

    for i in range(1, x+1):
        for j in range(1, y+1):
            if s1[i-1]==s2[j-1]:
                n[i][j] = n[i-1][j-1]+1
            elif n[i-1][j]>=n[i][j-1]:
                n[i][j]=n[i-1][j]
            else:
                n[i][j] = n[i][j-1]
    return n[x][y]

def commonChild2(s1, s2):
  maxAt = {}

  for i1 in range(len(s1)):
    maxForI1 = 0
    for i2 in range(len(s2)):
      potentialSum = maxForI1 + 1

      # You might be tempted to use the max() function to simplify the next three lines,
      # but that makes the solution so much slower that several of the test cases fail.
      other = maxAt.get(i2, 0)
      if other > maxForI1:
        maxForI1 = other

      if s1[i1] == s2[i2]:
        maxAt[i2] = potentialSum

  return max(maxAt.values(), default=0)

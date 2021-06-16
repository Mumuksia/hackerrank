#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

# Complete the substrCount function below.
def substrCount(n, s):
	odds = []
	tempOdds = []
	count = 0
	step = 0

	if n == 1:
		return 1

	if n > 2:
		for k in range(n):
			tempOdds.append(k)
	
		for i in range(n):
			odds = tempOdds
			tempOdds = []
			step +=1
			for j in range(len(odds)):
				if odds[j] - step >= 0 and odds[j] + step < n and (s[odds[j] - step] == s[odds[j] + step]) and (s[odds[j]-1] == s[odds[j] - step]):
					tempOdds.append(j)
					count +=1

	tempEven = []
	for i in range(1, n):
		if s[i] == s[i-1]:
			tempEven.append(i)
			count +=1
	

	

	step = 1
	for i in range(n):
		even = tempEven
		tempEven = []
		step +=2
		# print("State " + str(even) + " " + str(step))
		for j in range(len(even)):
			if (even[j] - step) >=0 and s[even[j] - step] == s[even[j] - step +1] and  s[even[j] - step] == s[even[j] - 1]:
				# print(j)
				tempEven.append(j)
				count +=1

	return count + n

def substrCount2(n, s):
    count = n
    for x in range(n): 
        y = x
        while y < n - 1:
            y += 1
            if s[x] == s[y]:
                count += 1
            else:
                if s[x:y] == s[y+1:2*y-x+1]:
                    count += 1
                break

    return count


print(substrCount(8, "mnonopoo"))   # 12
print(substrCount(5, "asasd"))   # 7
print(substrCount(7, "abcbaba"))   # 10
print(substrCount(4, "aaaa"))   # 10
print(substrCount(2, "aa"))   # 10
print(substrCount2(7, "aaabaaa"))   # 16
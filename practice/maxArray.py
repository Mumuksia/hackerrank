#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
	print(len(arr))
	if len(arr) > 10000:
		sys.setrecursionlimit(len(arr)*2)

	memo = [[-1 for _ in range(3)] for _ in range(len(arr)+1)]
	# print(memo)

	return max(step(arr, 0, 0, memo), step(arr, 0, 1, memo))
    	

def step(arr, i, r, memo):

	if (i >=len(arr)):
		return 0
	if memo[i][r] == -1:
		if r == 0:
			memo[i][r] = max(arr[i] + step(arr, i+1, 1, memo), step
				(arr, i+1, 0, memo))
		else:
			memo[i][r] = step(arr, i+1, 0, memo)

	return memo[i][r]

def check():
	f = open("maxArray.txt", "r")
	maxSubsetSum(list(map(int, f.read().rstrip().split())))

# print(maxSubsetSum([-1, 2, 3, 4])) # 6

# print(maxSubsetSum([2, 1, 5, 8, 4])) # 11

# print(maxSubsetSum([3, 7, 4, 6, 5])) # 13

print(maxSubsetSum([3, 5, -7, 8, 10])) # 15
# print(maxSubsetSum([-2, -3, -1])) # 0
# print(maxSubsetSum([1])) # 1
# print(maxSubsetSum([0, 0, 0, 0, -1, -1, -1])) # 0
# print(maxSubsetSum([0, 0, 0, 0, 100, 0])) # 100
print(maxSubsetSum([1, 9999, -9998])) # 9999


print(check()) # 99



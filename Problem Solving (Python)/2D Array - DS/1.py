#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    best = -99999
    for x in range(4):
        for y in range(4):
            total = 0
            total += arr[x][y]
            total += arr[x][y+1]
            total += arr[x][y+2]
            
            total += arr[x+1][y+1]
            
            total += arr[x+2][y]
            total += arr[x+2][y+1]
            total += arr[x+2][y+2]
            
            if total > best:
                best = total
    
    return best
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

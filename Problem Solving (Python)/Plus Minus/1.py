#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    ratioPos = 0
    positive = 0
    ratioNeg = 0
    negative = 0
    ratioZero = 0
    zeroNum = 0
    
    for num in arr:
        if num > 0:
            positive += 1
        elif num < 0:
            negative += 1
        elif num == 0:
            zeroNum += 1
            
    ratioPos = positive / len(arr)
    ratioNeg = negative / len(arr)
    ratioZero = zeroNum / len(arr)
    
    print("{:.6f}".format(ratioPos))
    print("{:.6f}".format(ratioNeg))
    print("{:.6f}".format(ratioZero))
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

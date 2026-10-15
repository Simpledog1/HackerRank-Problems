#!/bin/python3
import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    result = (datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z") - datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")).total_seconds()
    result = abs(int(result))
    return str(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

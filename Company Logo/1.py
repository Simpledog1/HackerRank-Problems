import math
import os
import random
import re
import sys

from collections import Counter

if __name__ == '__main__':
    s = input()
    counts = Counter(s)
    top_three = sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:3]

    for char, count in top_three:
        print(f"{char} {count}")

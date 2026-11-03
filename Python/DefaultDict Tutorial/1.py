# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
d = defaultdict(list)
n, m = map(int, input().split())
for i in range(1, n + 1):
    d[input()].append(i)
for i in range(1, m + 1):
    word = input()
    if word in d:
        print(" ".join(map(str, d[word])))
    else:
        print("-1")

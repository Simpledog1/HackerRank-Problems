# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
S, k= input().split()
k = int(k)

for y in range(1,k+1):
    for i in combinations(sorted(S),y):
        print("".join(i))

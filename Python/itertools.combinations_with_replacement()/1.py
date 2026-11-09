# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

S, k =input().split()
k = int(k)

S = sorted(S)

for i in combinations_with_replacement(S,k):
    print("".join(i))

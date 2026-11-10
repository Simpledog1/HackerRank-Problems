# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
S, k = input().split()
k = int(k)

for result in permutations(sorted(S),k):
    print("".join(result))
    

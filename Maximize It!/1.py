from itertools import product
k, m = map(int, input().split())

lists = []
maximum = 0

for combo in range(k):
    lists.append(list(map(int, input().split()[1:])))
    
for combo in product(*lists):
    sum(x**2 for x in combo) % m
    maximum = max(maximum, sum(x**2 for x in combo) % m)
    
print(maximum)

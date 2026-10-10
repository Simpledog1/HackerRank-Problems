from itertools import combinations

n = int(input())
a = list(input().split())
k = int(input())

result = list(combinations(a,k))
total = len(result)

count = 0

for combo in result:
    if 'a' in combo:
        count += 1
        
final = f"{count / total:.3f}"
print(final)

n, m = list(map(int, input().split()))
N = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

happiness = 0

for i in N:
    if i in A:
        happiness += 1
    elif i in B:
        happiness -= 1
        
print(happiness)

A = set(map(int, input().split()))
N = int(input())
result = True
for i in range(N):
    other = set(map(int, input().split()))
    if not A > other:
        result = False
print(result)

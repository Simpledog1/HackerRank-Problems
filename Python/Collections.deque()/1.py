from collections import deque
d = deque()
N = int(input())
for i in range(N):
    command = input().split()
    if command[0] == "append":
        d.append(command[1])
    if command[0] == "appendleft":
            d.appendleft(command[1])
    if command[0] == "pop":
            d.pop()
    if command[0] == "popleft":
            d.popleft()
for i in d:
    print(i, end=" ")
    

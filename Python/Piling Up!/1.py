from collections import deque

T = int(input())

for _ in range(T):
    n = int(input())
    blocks = deque(map(int, input().split()))

    top = float('inf')
    possible = True

    while blocks:
        if blocks[0] >= blocks[-1]:
            current = blocks[0]
        else:
            current = blocks[-1]

        if current > top:
            possible = False
            break

        top = current

        if current == blocks[0]:
            blocks.popleft()
        else:
            blocks.pop()

    print("Yes" if possible else "No")


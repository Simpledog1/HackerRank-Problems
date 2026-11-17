# Enter your code here. Read input from STDIN. Print output to STDOUT
A = int(input())
N = set(map(int, input().split()))
operations = int(input())

for _ in range(operations):
    operation = input().split()
    other = set(map(int, input().split()))

    command = operation[0]

    if command in ("update","|="):
        N.update(other)
    elif command in ("intersection_update", "&="):
        N.intersection_update(other)
    elif command in ("difference_update", "-="):
        N.difference_update(other)
    elif command in ("symmetric_difference_update", "^="):
        N.symmetric_difference_update(other)
print(sum(N))

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for i in range(n):
    a = int(input())
    A = set(map(int, input().split()))
    b = int(input())
    B = set(map(int, input().split()))
    
    result = True

    for i in A:
        if i not in B:
            result = False
    print(result)

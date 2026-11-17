# Enter your code here. Read input from STDIN. Print output to STDOUT
k = int(input())
K = set(map(int, input().split()))
n = int(input())
N = set(map(int, input().split()))

print(len(K.union(N)))

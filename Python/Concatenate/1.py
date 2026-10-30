# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
N, M, P = map(int, input().split())

A = []

for i in range(N):
    A.append(list(map(int, input().split())))

B = []

for i in range(M):
    B.append(list(map(int, input().split())))
    
print(numpy.concatenate((A,B)))

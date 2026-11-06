import numpy

N = int(input())

A = []
B = []
for i in range(N):
    A.append(numpy.array(list(map(int, input().split()))))
for i in range(N):
    B.append(numpy.array(list(map(int, input().split()))))
print(numpy.matmul(A, B))



import numpy
N = int(input())
A = []
for i in range(N):
    A.append(list(map(float, input().split())))
print(numpy.around(numpy.linalg.det(A), 2))
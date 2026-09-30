import numpy

N, M = list(map(int, input().split()))

A = []

for i in range(N):
    A.append(list(map(int, input().split())))

print(numpy.mean(A, axis = 1))
print(numpy.var(A, axis = 0))
print(numpy.around(numpy.std(A), 11))
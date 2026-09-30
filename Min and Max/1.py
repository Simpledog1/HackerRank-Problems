import numpy
N, M = list(map(int, input().split()))
A = []
for i in range(N):
    A.append(list(map(int, input().split())))

Min = numpy.min(A, axis = 1)
Max = numpy.max(Min)
print(Max)

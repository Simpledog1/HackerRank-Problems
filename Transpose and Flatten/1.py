import numpy

N, M = map(int, input().split())
A = []
for i in range(N):
    A.append(list(map(int, input().split())))

result = numpy.array(A)
print(numpy.transpose(result))
print(result.flatten())
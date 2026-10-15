import numpy
N, M = map(int, input().split())
A = []

for i in range(N):
    A.append(list(map(int, input().split())))

B = []

for i in range(N):
    B.append(list(map(int, input().split())))

A = numpy.array(A)
B = numpy.array(B)

print(A + B)
print(A - B)
print(A * B)
print(numpy.floor_divide(A, B))
print(A % B)
print(A ** B)
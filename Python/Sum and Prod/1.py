import numpy
N, M = map(int, input().split())
X = []
for i in range(N):
    X.append(numpy.array(list(map(int, input().split()))))
print (numpy.prod(sum(X), axis = 0)) 


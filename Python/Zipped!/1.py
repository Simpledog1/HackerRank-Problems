# Enter your code here. Read input from STDIN. Print output to STDOUT
n,x = map(int, input().split())

marks = []

for i in range(x):
    marks.append(list(map(float, input().split())))

for student in zip(*marks):
    print(sum(student)/len(student))

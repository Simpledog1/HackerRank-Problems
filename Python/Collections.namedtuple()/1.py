# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
N = int(input())
column_names = input().split()
Student = namedtuple("Student",column_names)
total = 0
for i in range(N):
    student = Student(*input().split())
    total += int(student.MARKS)
print(f"{total/N:.2f}")

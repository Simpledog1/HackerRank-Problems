# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
result = list(map(int, input().split()))
print(all(number > 0 for number in result) and any(str(number) == str(number)[::-1] for number in result ))

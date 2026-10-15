import re
N = int(input())

for i in range(N):
    
    S = input()
    result = re.findall(r"(?<=:| )#(?:[0-9A-Fa-f]{6}|[0-9A-Fa-f]{3})", S)
    
    for i in result:
        print(i)


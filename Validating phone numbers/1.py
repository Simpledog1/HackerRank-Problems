import re

S = int(input())

for i in range(S):

    N = input()

    result = re.match(r'^[789]\d{9}$', N)
    
    if result:
        print("YES")
    else:
        print("NO")
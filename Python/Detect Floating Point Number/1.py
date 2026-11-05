import re
N = int(input())
for i in range(N):
    string = input()
    if re.fullmatch(r"[+-]?\d*\.\d+", string):
        print(True)
    else:
        print(False)

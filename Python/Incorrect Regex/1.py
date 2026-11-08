# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
T = int(input())
for i in range(T):
    try:
        S = raw_input()
        re.compile(S)
        print(True)
    except re.error:
        print(False)

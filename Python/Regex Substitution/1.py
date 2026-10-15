import re

N = int(input())

for i in range(N):
    S = input()

    n = re.sub(r"(?<= )&&(?= )", "and", S)

    orange = re.sub(r"(?<= )\|\|(?= )", "or", n)

    print(orange)
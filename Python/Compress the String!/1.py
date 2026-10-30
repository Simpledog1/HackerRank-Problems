from itertools import groupby

S = input()

for key, group in groupby(S):
    print((len(list(group)), int(key)), end=" ")

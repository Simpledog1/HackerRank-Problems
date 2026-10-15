import re

S = input()
k = input()

m = re.finditer(r'(?=(' + k + '))',S)

found = False

for i in m:
    found = True
    end = i.start() + len(k) - 1
    print((i.start(), end))
    
if not found:
    print((-1, -1))

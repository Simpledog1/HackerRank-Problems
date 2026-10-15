import re
from email.utils import parseaddr, formataddr

N = int(input())

for i in range(N):

    line = input()
    name, email = parseaddr(line)

    result = re.match(r'^[A-Za-z][A-Za-z0-9._-]*@[A-Za-z]+\.[A-Za-z]{1,3}$', email)
    
    if result:
        print(formataddr((name, email)))

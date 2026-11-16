n = int(input())
s = set(map(int, input().split()))
counter = int(input())
count = 0
while count < counter:
    x = input()
    count += 1
    parts = x.split()
    action = parts[0]
    if action == "pop":
        s.pop() 
    elif action == "remove":
        num = int(parts[1])
        s.remove(num)
    elif action == "discard":
        num = int(parts[1])
        s.discard(num)
print(sum(s))
        
    
    

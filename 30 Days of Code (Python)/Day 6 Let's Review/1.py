# Enter your code here. Read input from STDIN. Print output to STDOUT 
t = int(input())
for _ in range(t):
    s = input()
    even_index = ""
    odd_index = ""
    for i in range(len(s)):
        if i % 2 == 0:
            even_index += s[i]
        else:
            odd_index += s[i]
    
    print(even_index, odd_index)

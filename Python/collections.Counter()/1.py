# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
num_of_shoes = int(input())
list_of_shoe_size = Counter(map(int, input().split()))
Customers = int(input())

total = 0
for i in range(Customers):
    shoe_size, price = map(int, input().split())
    if list_of_shoe_size[shoe_size] != 0:
        total += price
        list_of_shoe_size[shoe_size] -= 1
print(total)

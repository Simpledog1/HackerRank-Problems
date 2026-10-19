number_count = {}
N = int(input())

for i in range(N):

    number = int(input())
    if number in number_count:
        number_count[number] += 1
    else:
        number_count[number] = 1

print(number_count)
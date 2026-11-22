K = int(input())
room_number = list(map(int, input().split()))

count = {}

for i in room_number:
    if i not in count:
        count[i] = 1
    else:
        count[i] += 1

for room in count:
    if count[room] == 1:
        print(room)

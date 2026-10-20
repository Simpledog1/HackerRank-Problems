word_count = {}
N = int(input())

for i in range(N):
    word = input()

    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(len(word_count))

for word, count in word_count.items():
    print(count, end=" ")

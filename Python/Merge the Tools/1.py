s = "AAB"
k = 3

seen = set()
result = ""

for i in range(0, len(s), k):
    chunk = s[i: i + k]

    for item in chunk:
        if item in seen:
            continue

        seen.add(item)
        result += item

    print(result)
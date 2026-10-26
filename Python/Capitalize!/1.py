

# Complete the solve function below.
def solve(s):
    words = s.split(" ")
    for i in range(len(words)):
        if words[i]:
            words[i] = words[i][0].upper() + words[i][1:]
    return " ".join(words)


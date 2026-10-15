T = int(input())

for i in range(T):
    uid = input()

    uppercase_count = 0
    number_count = 0
    valid = True
    seen = set()

    for letter in uid:
        if letter.isupper():
            uppercase_count += 1

        if letter.isdigit():
            number_count += 1

        if not letter.isalnum():
            valid = False

        if letter in seen:
            valid = False
        else:
            seen.add(letter)

    if valid == True and uppercase_count >= 2 and number_count >= 3 and len(uid) == 10:
        print("Valid")
    else:
        print("Invalid")
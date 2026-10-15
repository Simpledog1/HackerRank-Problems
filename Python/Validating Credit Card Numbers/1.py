import re

T = int(input())

for i in range(T):
    card = input()

    digits = card.replace("-", "")

    pattern = r"^([456]\d{15}|[456]\d{3}-\d{4}-\d{4}-\d{4})$"

    if not re.fullmatch(pattern, card):
        print("Invalid")
    elif re.search(r"(\d)\1{3,}", digits):
        print("Invalid")
    else:
        print("Valid")


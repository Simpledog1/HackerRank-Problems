import string

def print_rangoli(size):
    letters = string.ascii_lowercase
    width = 4 * size - 3

    lines = []
    
    for i in range(size):
        left = letters[size - 1:i:-1]
        right = letters[i:size]
        row = "-".join(left + right)
        lines.append(row.center(width, "-"))

    print("\n".join(lines[::-1] + lines[1:]))


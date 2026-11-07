def count_substring(string, sub_string):
    result = 0
    for letter in range(0, len(string)):
        if string[letter: letter + len(sub_string)] == sub_string:
            result += 1
    return result

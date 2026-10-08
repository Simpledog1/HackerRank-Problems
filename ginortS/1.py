S = input()

result_lower = []
result_upper = []
result_odd = []
result_even = []

for letter in S:
    if letter.islower():
        result_lower.append(letter)
        
    if letter.isupper():
        result_upper.append(letter)
            
            
    if letter.isdigit():
        if int(letter) % 2 != 0:
            result_odd.append(letter)
                
        if int(letter) % 2 == 0:
            result_even.append(letter)
        
result_lower.sort()
result_upper.sort()
result_odd.sort()
result_even.sort()

final = []

final.extend(result_lower)
final.extend(result_upper)
final.extend(result_odd)
final.extend(result_even)

print("".join(final))


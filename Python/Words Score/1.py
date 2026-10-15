total_score = 0
vowels = ("a","e","i","o","u","y")

n = int(input())
words = input().split()

for i in words:
    vowel_count = 0

    for letter in i:
        if letter in vowels:
            vowel_count += 1
    
    if vowel_count % 2 == 0:
        total_score += 2
        
    elif vowel_count % 2 != 0:
        total_score += 1
            
print(total_score)

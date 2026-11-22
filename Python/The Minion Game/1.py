def minion_game(string):
    # your code goes here
    kevin = 0
    stuart = 0
    for i in range(len(string)):
        if string[i] in "AEIOU":
            kevin += len(string) - i
        else:
            stuart += len(string) - i
    if kevin > stuart:
        print("Kevin", kevin)
    elif kevin < stuart:
        print("Stuart", stuart)
    else:
        print("Draw")


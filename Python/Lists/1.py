if __name__ == '__main__':
    N = int(input())
    result = []
    for _ in range(N):
        commands = input()
        parts = commands.split()
        if parts[0] == "print":
            print(result)
        elif parts[0] == "insert":
            result.insert(int(parts[1]),int(parts[2]))
        elif parts[0] == "remove":
            result.remove(int(parts[1]))
        elif parts[0] == "append":
            result.append(int(parts[1]))
        elif parts[0] == "sort":
            result.sort()
        elif parts[0] == "pop":
            result.pop()
        elif parts[0] == "reverse":
            result.reverse()
                                    
            
    

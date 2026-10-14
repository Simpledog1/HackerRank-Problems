def wrapper(f):
    def fun(l):
        numbers = []

        for number in l:
            number = number[-10:]
            result = "+91 " + number[:5] + " " + number[-5:]
            numbers.append(result)

        return f(numbers)

    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)

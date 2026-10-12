class EvenStream:
    def __init__(self):
        self.current = 0

    def get_next(self):
        ret = self.current
        self.current += 2
        return ret

class OddStream:
    def __init__(self):
        self.current = 1

    def get_next(self):
        ret = self.current
        self.current += 2
        return ret

def print_from_stream(n, stream=None):
    if stream is None:
        stream = EvenStream()
        
    for i in range(n):
        print(stream.get_next())
        
if __name__ == '__main__':
    queries = int(input())
    for _ in range(queries):
        stream_name, n = input().split()
        n = int(n)

        if stream_name == "even":
            print_from_stream(n)
        else:
            print_from_stream(n, OddStream())

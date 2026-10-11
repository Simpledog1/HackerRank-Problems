from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if "\n" in data:
            print(">>> Multi-line Comment")
            print(data)
        else:
            print(">>> Single-line Comment")
            print(data)
    def handle_data(self, data):
        if data != '\n':
            print(">>> Data")
            print(data)
            
N = int(input())
parser = MyHTMLParser()

parse_list = []

for i in range(N):
    html_line = input()
    parse_list.append(html_line)
combined = "\n".join(parse_list)
parser.feed(combined)
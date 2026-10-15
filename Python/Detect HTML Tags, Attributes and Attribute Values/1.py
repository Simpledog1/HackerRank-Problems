from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)

        for name, value in attrs:
            print(f"-> {name} > {value}")

N = int(input())
parser = MyHTMLParser()
parse_list = []

for i in range(N):
    html_line = input()
    parse_list.append(html_line)

combined = "\n".join(parse_list)
parser.feed(combined)
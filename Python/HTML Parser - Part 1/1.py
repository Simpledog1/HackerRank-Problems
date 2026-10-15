from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        
        for name, value in attrs:
            print(f"-> {name} > {value}")
            
    def handle_endtag(self, tag):
        print("End   :", tag)
        
    def handle_startendtag(self,tag, attrs):
        print("Empty :", tag)
        
        for name, value in attrs:
            print(f"-> {name} > {value}")

N = int(input())
parser = MyHTMLParser()
for i in range(N):
    html_line = input()
    parser.feed(html_line)
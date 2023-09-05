import requests
from html.parser import HTMLParser

def download_file():
    url = 'http://si-rdtest1:9090/job/CheckBuild/job/PreCheck_main/5834/flowGraphTable/'

    # download the picture through byte stream
    response = requests.get(url, stream=True)

    with open('test.html', 'wb') as file:
        for data in response.iter_content(128):
            file.write(data)
    print(response.status_code)


class MyHTMLParser(HTMLParser):
    # def handle_starttag(self, tag, attrs):
    #     print("Encountered a start tag:", tag)

    # def handle_endtag(self, tag):
    #     print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)
        with open("./initData.txt",'a') as f1:
            f1.write(data)
            

download_file()
with open("./test.html") as f:
    content = f.read()

parser = MyHTMLParser()
parser.feed(content)


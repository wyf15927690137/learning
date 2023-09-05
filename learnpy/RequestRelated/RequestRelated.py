import requests
import justext

response = requests.get("http://si-rdtest1:9090/job/CheckBuild/job/PreCheck_main/5834/flowGraphTable/")
paragraphs = justext.justext(response.content, justext.get_stoplist("English"))
for paragraph in paragraphs:
    print (paragraph.text)
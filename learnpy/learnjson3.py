import json

with open("./record.json","r") as load_f:
    dic = json.load(load_f)
    print(dic)
    print(type(dic))
import json

new_dic = {'one':1, 'two':{2.1:['a', 'b']}}
with open("./record1.json","w") as write_f:
    json.dump(new_dic,write_f,indent=4,ensure_ascii=False)

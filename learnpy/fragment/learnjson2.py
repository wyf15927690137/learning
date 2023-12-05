import json

new_dic = {'one':1, 'two':{2.1:['a', 'b']}}

with open("./record.json","w") as f:
    json.dump(new_dic,f)
    print("complete")